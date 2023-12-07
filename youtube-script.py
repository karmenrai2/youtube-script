import json

channel_num = int(input("How many channels should display?: "))
video_num = int(input("How many videos should display?: "))

# Load the JSON data from the Google Takeout file
with open('watch-history.json', 'r') as file:
    data = json.load(file)

# Create a dictionary to store channel views
channel_views = {}
video_views = {}


# Iterate through the JSON data
for item in data:
    if item.get('header') == 'YouTube':
        video_title = item.get('title')
        subtitles = item.get('subtitles', [])
        for subtitle in subtitles:
            channel_name = subtitle.get('name')
            if channel_name:
                channel_views[channel_name] = channel_views.get(channel_name, 0) + 1

for item in data:
    if item.get('header') == 'YouTube':
        video_title = item.get('title')
        subtitles = item.get('subtitles', [])
        for subtitle in subtitles:
            channel_name = subtitle.get('name')
            if channel_name != "From Google Ads":
                if video_title != "Answered survey question":
                    video_views[video_title] = video_views.get(video_title, 0) + 1


# Sort the channels by views in descending order
sorted_channels = sorted(channel_views.items(), key=lambda x: x[1], reverse=True)
sorted_videos = sorted(video_views.items(), key=lambda x: x[1], reverse=True)


# Print the top most-watched channels
print("Top YouTube Channels: ")
for i, (channel, views) in enumerate(sorted_channels[:channel_num]):
    print("{0}. {1}: {2} videos watched".format(i + 1, channel, views))

print("\n\n\n\n\n")

print("Top YouTube Videos: ")
for i, (video, vviews) in enumerate(sorted_videos[:video_num]):
    print("{0}. {1}: {2} times watched".format(i + 1, video, vviews))