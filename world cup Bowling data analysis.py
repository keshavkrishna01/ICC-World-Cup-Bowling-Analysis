#!/usr/bin/env python
# coding: utf-8

# # World Cup Bowling Data Analysis

# ![th.jpg](attachment:th.jpg)

# ### 01.Import Data and libraries

# In[2]:


import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np


# In[3]:


df=pd.read_csv('01_icc_wc_23_bowl.csv')
df.head()


# In[4]:


df.tail()


# In[5]:


df.isnull().sum()


# In[6]:


df.info()


# In[7]:


df.describe()


# In[8]:


df['team'].value_counts()


# ### 02. Data analysis

# In[9]:


player_name=df.loc[df['runs'].idxmax(),'player']
team_name=df.loc[df['runs'].idxmax(),'team']
highest_runs=df.loc[df['runs'].idxmax(),'runs']
opponent=df.loc[df['runs'].idxmax(),'opponent']

print("----> Highest runs were given by the bowler '",player_name, "' from the team of '", team_name, "' in one spell which are ",highest_runs, "against team ",opponent)

player_name=df.loc[df['wickets'].idxmax(),'player']
team_name=df.loc[df['wickets'].idxmax(),'team']
wickets=df.loc[df['wickets'].idxmax(),'wickets']
opponent=df.loc[df['wickets'].idxmax(),'opponent']

print("----> Highest wickets were taken by the bowler '",player_name, "' from the team of '", team_name, "' in one spell which are ",wickets, "against team ",opponent)

player_name=df.loc[df['6s'].idxmax(),'player']
team_name=df.loc[df['6s'].idxmax(),'team']
highest_6s=df.loc[df['6s'].idxmax(),'6s']
opponent=df.loc[df['6s'].idxmax(),'opponent']
print("----> Highest 6s were given by the bowler '",player_name, "' from the team of '", team_name, "' in one spell which are ",highest_6s, "against team ",opponent)

player_name=df.loc[df['4s'].idxmax(),'player']
team_name=df.loc[df['4s'].idxmax(),'team']
highest_4s=df.loc[df['4s'].idxmax(),'4s']
opponent=df.loc[df['4s'].idxmax(),'opponent']
print("----> Highest 4s were given by the bowler '",player_name, "' from the team of '", team_name, "' in one spell which are ",highest_4s, "against team ",opponent)

player_name=df.loc[df['maidens'].idxmax(),'player']
team_name=df.loc[df['maidens'].idxmax(),'team']
highest_maidens=df.loc[df['maidens'].idxmax(),'maidens']
opponent=df.loc[df['maidens'].idxmax(),'opponent']
print("----> Highest maidens were overed by the bowler '",player_name, "' from the team of '", team_name, "' in one spell which are ",highest_maidens, "against team ",opponent)


# In[10]:


# group the players by the overs, runs, wickets.....
df_player_overs=df.groupby('player').agg({'overs':'sum', 'maidens':'sum', 'runs':'sum', 'wickets':'sum', 'run_rate':'mean', '4s':'sum', '6s':'sum', 'wd':'sum'}).reset_index()


# In[11]:


# sort the dataset by the overs
sorted_df_player_overs = df_player_overs.sort_values(by='overs', ascending=False).reset_index()


# In[12]:


sorted_df_player_overs


# ### 03. Plot the bar graph between overs and players

# In[13]:


df_player_overs_top_30=sorted_df_player_overs.head(30)

# Plotting
plt.figure(figsize=(20, 6))
plt.bar(df_player_overs_top_30['player'], df_player_overs_top_30['overs'])
plt.xlabel('Player',fontsize=15,color='c')
plt.ylabel('overs',fontsize=15,color='c')
plt.title('Overs by the top 30 players',fontsize=20,color='g')
plt.xticks(rotation=45, ha='right')  # Rotate player names for better visibility
plt.tight_layout()

# Show the plot
plt.grid()
plt.show()


# ### 04. Runs given by the top 30 bowlers

# In[14]:


df_player_overs_top_30=sorted_df_player_overs.head(30)

# Plotting
plt.figure(figsize=(15, 6))
plt.bar(df_player_overs_top_30['player'], df_player_overs_top_30['runs'], color='violet')
plt.xlabel('Player',fontsize=15,color='c')
plt.ylabel('runs',fontsize=15,color='c')
plt.title('Runs given by the top 30 bowlers',fontsize=20,color='g')
plt.xticks(rotation=45, ha='right')  # Rotate player names for better visibility
plt.tight_layout()

# Show the plot
plt.grid()
plt.show()


# ### 05. Run_rate from the top 30 bowlers

# In[15]:


df_player_overs_top_30=sorted_df_player_overs.head(30)

# Plotting
plt.figure(figsize=(15, 6))
plt.bar(df_player_overs_top_30['player'], df_player_overs_top_30['run_rate'], color='orange')
plt.xlabel('Player',fontsize=15,color='c')
plt.ylabel('Run_rate',fontsize=15,color='c')
plt.title('Run_rate from the top 30 bowlers',fontsize=20,color='g')
plt.xticks(rotation=45, ha='right')  # Rotate player names for better visibility
plt.tight_layout()

# Show the plot
plt.grid()
plt.show()


# ### 06. Wide Balls from the top 30 bowlers

# In[16]:


df_player_overs_top_30=sorted_df_player_overs.head(30)

# Plotting
plt.figure(figsize=(15, 6))
plt.bar(df_player_overs_top_30['player'], df_player_overs_top_30['wd'], color='pink')
plt.xlabel('Player',fontsize=15,color='c')
plt.ylabel('Wide balls',fontsize=15,color='c')
plt.title('Wide balls from the top 30 bowlers',fontsize=20,color='g')
plt.xticks(rotation=45, ha='right')  # Rotate player names for better visibility
plt.tight_layout()

# Show the plot
plt.grid()
plt.show()


# ### 07. Maiden overs and Overs for the top 30 players

# In[17]:


fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot bars for 'overs' on the primary y-axis (ax1)

index = np.arange(len(df_player_overs_top_30))
bars = ax1.bar(index, df_player_overs_top_30['overs'], label='Overs', color='skyblue')

# Plot line for 'wickets' on the same y-axis (ax1)
line = ax1.plot(index, df_player_overs_top_30['maidens'], color='orange', marker='o', label='maidens')

# Set labels and titles
ax1.set_xlabel('Player')
ax1.set_ylabel('Overs', color='skyblue')
ax1.tick_params(axis='y', labelcolor='skyblue')  # Make sure y-axis labels are in blue

plt.title('Maiden overs and Overs for the top 30 players')

# Combine legends
bars_legend = [bar for bar in bars]
line_legend = [line[0]]
plt.legend(bars_legend + line_legend, ['Overs', 'Maiden '], loc='upper left')

# Set x-axis ticks and labels
plt.xticks(index, df_player_overs_top_30['player'], rotation=45, ha='right')

# Show the plot\
plt.legend()
plt.tight_layout()
plt.grid()
plt.show()


# ### 08. Bowlers are sorted on the wickets taken by them

# In[18]:


sorted_df_player_wickets = df_player_overs.sort_values(by='wickets', ascending=False).reset_index()
sorted_df_player_wickets


# ### 09. Wickets taken by the top 30 bowlers

# In[19]:


df_player_wickets_top_30=sorted_df_player_wickets.head(30)

# Plotting
plt.figure(figsize=(15, 6))
plt.bar(df_player_wickets_top_30['player'], df_player_wickets_top_30['wickets'], color='violet')
plt.xlabel('Player',fontsize=15,color='c')
plt.ylabel('Wickets',fontsize=15,color='c')
plt.title('wickets taken by the top 30 bowlers',fontsize=20,color='g')
plt.xticks(rotation=45, ha='right')  # Rotate player names for better visibility
plt.tight_layout()

# Show the plot
plt.grid()
plt.show()


# ### 10. Wickets and Overs for the top 30 players

# In[20]:


# Create a figure and axis
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot bars for 'overs' on the primary y-axis (ax1)

index = np.arange(len(df_player_wickets_top_30))
bars = ax1.bar(index, df_player_wickets_top_30['overs'], label='Overs', color='skyblue')

# Plot line for 'wickets' on the same y-axis (ax1)
line = ax1.plot(index, df_player_wickets_top_30['wickets'], color='orange', marker='o', label='Wickets')

# Set labels and titles
ax1.set_xlabel('Player',fontsize=15,color='c')
ax1.set_ylabel('Overs', color='skyblue',fontsize=15)
ax1.tick_params(axis='y', labelcolor='skyblue')  # Make sure y-axis labels are in blue

plt.title('Wickets and Overs for the top 30 players',fontsize=20,color='g')

# Combine legends
bars_legend = [bar for bar in bars]
line_legend = [line[0]]
plt.legend(bars_legend + line_legend, ['Overs', 'Wickets'], loc='upper left')

# Set x-axis ticks and labels
plt.xticks(index, df_player_wickets_top_30['player'], rotation=45, ha='right')

# Show the plot
plt.legend()
plt.tight_layout()
plt.grid()
plt.show()


# ### 11. 4s given by the top 30 bowlers

# In[21]:


df_player_wickets_top_30=sorted_df_player_wickets.head(30)

# Plotting
plt.figure(figsize=(15, 6))
plt.bar(df_player_wickets_top_30['player'], df_player_wickets_top_30['4s'], color='cyan')
plt.xlabel('Player',fontsize=15,color='c')
plt.ylabel('No of 4s given',fontsize=15,color='c')
plt.title('4s given by the top 30 bowlers',fontsize=20,color='black')
plt.xticks(rotation=45, ha='right')  # Rotate player names for better visibility
plt.tight_layout()

# Show the plot
plt.grid()
plt.show()


# ### 12. 6s Given by the top 30 Bowlers

# In[22]:


plt.figure(figsize=(15,6))
plt.plot(df_player_wickets_top_30['player'], df_player_wickets_top_30['6s'], marker='o', linestyle='--')
plt.grid()
plt.gray()
plt.xlabel('Player',fontsize=15,color='c')
plt.ylabel('6s given by bowlers',fontsize=15,color='c')
plt.title('6s given by the top 30 bowlers',fontsize=20,color='gray')
plt.xticks(rotation=45, ha='right')  # Rotate player names for better visibility
plt.tight_layout()

# Show the plot
plt.show()
plt.show()


# ### Group by Team 

# In[23]:


df_team_overs=df.groupby('team').agg({'overs':'sum', 'maidens':'sum', 'runs':'sum', 'wickets':'sum', 'run_rate':'mean', '4s':'sum', '6s':'sum', 'wd':'sum'}).reset_index()
df_team_overs


# ### 13. Overs by each Team

# In[24]:


# Plotting
plt.figure(figsize=(10, 6))
plt.bar(df_team_overs['team'], df_team_overs['overs'], color='gray')
plt.xlabel('Team',fontsize=15,color='black')
plt.ylabel('Overs',fontsize=15,color='black')
plt.title('Overs by each Team',fontsize=15,color='black')
plt.xticks(rotation=45, ha='right')  # Rotate player names for better visibility
plt.tight_layout()

# Show the plot
plt.grid()
plt.show()


# ### 14. Maiden overs by each Team

# In[25]:


# Plotting
plt.figure(figsize=(10, 6))
plt.bar(df_team_overs['team'], df_team_overs['maidens'])
plt.xlabel('Team',fontsize=15)
plt.ylabel('Maiden overs',fontsize=15)
plt.title('Maiden overs by each Team',fontsize=15)
plt.xticks(rotation=45, ha='right')  # Rotate player names for better visibility
plt.tight_layout()

# Show the plot
plt.grid()
plt.show()


# ### 15. Run_rate by the Team Bowlers

# In[26]:


plt.figure(figsize=(12,6))
plt.plot(df_team_overs['team'], df_team_overs['run_rate'], marker='o', linestyle='--')
plt.grid()
plt.gray()
plt.xlabel('Teams')
plt.ylabel('run_rate')
plt.title('Run_rate by the Team bowlers')
plt.xticks(rotation=45, ha='right')  # Rotate player names for better visibility
plt.tight_layout()

# Show the plot
plt.show()
plt.show()
plt.show()


# ### 16. Wickets taken by Each Team

# In[27]:


plt.figure(figsize=(8, 8))
ex=[0.0,0.0,0.0,0.0,0.3,0.0,0.0,0.0,0.0,0.0]
plt.pie(df_team_overs['wickets'],explode=ex, labels=df_team_overs['team'],autopct='%0.2f%%',wedgeprops={"edgecolor":"m"})
plt.title('Wickets taken by Each Team')
# plt.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.

plt.show()


# ### 17. Wickets taken by Each Team

# In[30]:


plt.figure(figsize=(15,6))
plt.plot(df_team_overs['team'], df_team_overs['runs'], marker='o', linestyle='--')
plt.grid()
plt.gray()
plt.xlabel('Teams')
plt.ylabel('runs')
plt.title('Runs given by the Team bowlers')
plt.xticks(rotation=45, ha='right')  # Rotate player names for better visibility
plt.tight_layout()

# Show the plot
plt.show()
plt.show()
plt.show()
plt.show()


# ### 18. Wides by Each Team

# In[29]:


plt.figure(figsize=(8, 8))

ex=[0.0,0.0,0.0,0.0,0.3,0.0,0.0,0.0,0.0,0.0]
plt.pie(df_team_overs['wd'], labels=df_team_overs['team'],explode=ex,autopct='%0.2f%%',wedgeprops={"edgecolor":"c"})
plt.title('Wides by Each Team')
# plt.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.

plt.show()


# In[ ]:




