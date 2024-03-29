
import instaloader
import pandas as pd
import math 
import scipy.stats as stats

df = pd.DataFrame()

bot = instaloader.Instaloader()

profile = instaloader.Profile.from_username(bot.context, 'nosettacomo')


for post in profile.get_posts():
    newData = {'NumLikes': post.likes, 'Comments': post.comments, 'Caption' : post.caption, 'Hashtags' : post.caption_hashtags, 'Mentions': post.caption_mentions
               , 'Date': post.date , 'IsVideo': post.is_video, 'VideoLength': post.video_duration, 'VideoViews': post.video_view_count}
    df = df.append(newData, ignore_index= True)
    
    
df.to_csv("nosettaIGData.csv")
