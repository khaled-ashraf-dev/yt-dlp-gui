# Import necessary modules
from yt_dlp import YoutubeDL
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

"""
YouTube Downloader GUI

This script creates a graphical user interface (GUI) for a YouTube video and playlist downloader using the yt-dlp library.
Users can select various download options, including metadata, subtitles, comments, thumbnail, and more. 
They can also set playlist parameters such as start, end, minimum views, and maximum views. 
The script allows users to choose the video resolution and provides a button to initiate the download process.

Dependencies:
- yt-dlp: A YouTube video downloader library
- ttkbootstrap: A Bootstrap-themed tkinter library for GUI design
- ttkbootstrap.constants: Constants used for ttkbootstrap theming

Author: Khaled Ashraf
Date: September 27th 2023
"""


# Create the main application window
root = ttk.Window(themename="vapor", title='Youtube Downloader')

# Create IntVar variables to store checkbox values
c_simulate_var = ttk.IntVar()
c_subs_var = ttk.IntVar()
c_json_var = ttk.IntVar()
c_comments_var = ttk.IntVar()
c_thumbnail_var = ttk.IntVar()
c_desc_var = ttk.IntVar()
c_error_var = ttk.IntVar()
c_random_var = ttk.IntVar()
c_reverse_var = ttk.IntVar()

# Create StringVar variables to store text entry values
e_start_var = ttk.StringVar()
e_end_var = ttk.StringVar()
e_min_var = ttk.StringVar()
e_max_var = ttk.StringVar()
e_url_var = ttk.StringVar()
m_res_var = ttk.StringVar()

# Function to write selected options and start the download
def write_values():
    # List of boolean options mapped to their respective IntVar variables
    bool_opts = [c_simulate_var.get(), c_subs_var.get(),
                 c_json_var.get(), c_comments_var.get(),
                 c_thumbnail_var.get(), c_desc_var.get(),
                 c_random_var.get(), c_error_var.get(),
                 c_reverse_var.get()]

    # Corresponding yt-dlp option names
    yt_dlp_opts = ['simulate', 'writesubtitles', 'writeinfojson',
                   'getcomments', 'writethumbnail', 'writedescription',
                   'ignoreerrors', 'playlistrandom', 'playlistreverse']

    # Create an empty dictionary to store selected options
    ydl_opts = {}

    # Populate the ydl_opts dictionary based on selected options
    for i in range(len(yt_dlp_opts)):
        if bool_opts[i]:
            ydl_opts[yt_dlp_opts[i]] = True
        else:
            ydl_opts[yt_dlp_opts[i]] = False

    # List of entry values mapped to their respective StringVar variables
    entry_opts = [e_start_var.get(), e_end_var.get(), e_min_var.get(),
                  e_max_var.get()]

    # Corresponding yt-dlp entry option names
    yt_dlp_entry_opts = ['playliststart', 'playlistend', 'min_views',
                         'max_views']

    # Populate the ydl_opts dictionary with entry options as integers
    for i in range(len(yt_dlp_entry_opts)):
        if entry_opts[i]:
            ydl_opts[yt_dlp_entry_opts[i]] = int(entry_opts[i])

    # Set the 'format' option based on selected video resolution
    if m_res_var.get() == ' 240p':
        ydl_opts['format'] = '[height<=240]+worstaudio'
    elif m_res_var.get() == ' 360p':
        ydl_opts['format'] = '[height<=360]+worstaudio'
    elif m_res_var.get() == ' 480p':
        ydl_opts['format'] = '[height<=480]+worstaudio'
    elif m_res_var.get() == ' 720p':
        ydl_opts['format'] = '[height<=720]+worstaudio'
    elif m_res_var.get() == ' Audio':
        ydl_opts['format'] = 'worstaudio'

    # Use yt-dlp to start the download
    with YoutubeDL(ydl_opts) as ydl:
        print('hello')
        ydl.download([e_url_var.get()])

# Create and configure Metadata label
l_meta = ttk.Label(text='Metadata', bootstyle="light")
l_meta.grid(row=0, column=1, padx=30, pady=15)

# Create and configure various checkboxes and labels for options and settings
# Note: Each widget is positioned using grid(row, column) and aligned with sticky='w' (west)
c_simulate = ttk.Checkbutton(
    root, text='Simulate', bootstyle="round-toggle", variable=c_simulate_var)
c_simulate.grid(row=1, column=0, padx=30, pady=10, sticky='w')

c_subs = ttk.Checkbutton(root, text='Download Subtitles',
                         bootstyle="round-toggle", variable=c_subs_var)
c_subs.grid(row=1, column=1, padx=30, pady=10, sticky='w')

c_json = ttk.Checkbutton(root, text='Export Json',
                         bootstyle="round-toggle", variable=c_json_var)
c_json.grid(row=1, column=2, padx=30, pady=10, sticky='w')

c_comments = ttk.Checkbutton(
    root, text='Download Comments', bootstyle="round-toggle", variable=c_comments_var)
c_comments.grid(row=2, column=0, padx=30, pady=10, sticky='w')

c_thumbnail = ttk.Checkbutton(
    root, text='Download Thumbnail', bootstyle="round-toggle", variable=c_thumbnail_var)
c_thumbnail.grid(row=2, column=1, padx=30, pady=10, sticky='w')

c_desc = ttk.Checkbutton(root, text='Get Description',
                         bootstyle="round-toggle", variable=c_desc_var)
c_desc.grid(row=2, column=2, padx=30, pady=10, sticky='w')

# Create and configure label for Playlist Options
l_playlist = ttk.Label(text='Playlist Options', bootstyle="light")
l_playlist.grid(row=3, column=1, padx=30, pady=15)

# Create and configure various checkboxes for playlist options
c_archive = ttk.Checkbutton(
    root, text='Ignore Errors', bootstyle="round-toggle", variable=c_error_var)
c_archive.grid(row=4, column=0, padx=30, pady=10, sticky='w')

c_random = ttk.Checkbutton(root, text='Download in Random Order',
                           bootstyle="round-toggle", variable=c_random_var)
c_random.grid(row=4, column=1, padx=30, pady=10, sticky='w')

c_reverse = ttk.Checkbutton(root, text='Download in Reverse Order',
                            bootstyle="round-toggle", variable=c_reverse_var)
c_reverse.grid(row=4, column=2, padx=30, pady=10, sticky='w')

# Create and configure labels and text entry fields for playlist settings
l_start = ttk.Label(text='Playlist Start', bootstyle="light")
l_start.grid(row=5, column=0, padx=30, pady=10)

e_start = ttk.Entry(bootstyle="light", textvariable=e_start_var)
e_start.grid(row=5, column=1, padx=30, pady=10)

l_end = ttk.Label(text='Playlist End', bootstyle="light")
l_end.grid(row=6, column=0, padx=30, pady=10)

e_end = ttk.Entry(bootstyle="light", textvariable=e_end_var)
e_end.grid(row=6, column=1, padx=30, pady=10)

l_min = ttk.Label(text='Minimum Views', bootstyle="light")
l_min.grid(row=7, column=0, padx=30, pady=10)

e_min = ttk.Entry(bootstyle="light", textvariable=e_min_var)
e_min.grid(row=7, column=1, padx=30, pady=10)

l_max = ttk.Label(text='Maximum Views', bootstyle="light")
l_max.grid(row=8, column=0, padx=30, pady=10)

e_max = ttk.Entry(bootstyle="light", textvariable=e_max_var)
e_max.grid(row=8, column=1, padx=30, pady=10)

# Create and configure labels and Combobox for video resolution settings
l_format = ttk.Label(text='Format', bootstyle="light")
l_format.grid(row=9, column=1, padx=30, pady=15)

l_res = ttk.Label(text='Video Resolution', bootstyle="light")
l_res.grid(row=10, column=0, padx=30, pady=10)

m_res = ttk.Combobox(bootstyle="info", width=20, textvariable=m_res_var)
m_res.grid(row=10, column=1, padx=30, pady=10, sticky='w')
m_res['values'] = [' 240p', ' 360p', ' 480p', ' 720p', ' Audio']
m_res.current(3)

# Create and configure labels and text entry fields for playlist URL and download button
l_url = ttk.Label(text='Playlist URL', bootstyle="light")
l_url.grid(row=11, column=0, padx=30, pady=10)

e_url = ttk.Entry(bootstyle="light", textvariable=e_url_var)
e_url.grid(row=11, column=1, columnspan=2, padx=30, pady=10, sticky='ew')

b_download = ttk.Button(root, text='Start Download',
                        bootstyle=SECONDARY, command=write_values)
b_download.grid(row=12, column=1, padx=30, pady=10)

# Start the main application loop
root.mainloop()
