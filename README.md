# youtube_url_in_video
This is the code used to get a YouTube video to have its own URL, which has also been slightly modified to support the more general use case of uploading x bytes of one video file and the rest of the bytes from another video file.

This uses YouTube API's resumable upload feature (https://developers.google.com/youtube/v3/guides/using_resumable_upload_protocol), more specifically the chunked uploading process, and quite a bit of manual fiddling with files to get them to have the same first bytes as well as size.
