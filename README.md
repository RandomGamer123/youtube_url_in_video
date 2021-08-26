# youtube_url_in_video
This is the code used to get a YouTube video to have its own URL.

This uses YouTube API's resumable upload feature (https://developers.google.com/youtube/v3/guides/using_resumable_upload_protocol), more specifically the chunked uploading process, and quite a bit of manual fiddling with files to get them to have the same first bytes as well as size.
