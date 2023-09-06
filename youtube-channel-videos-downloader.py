import os
from pytube import YouTube

def download_video(url, output_folder):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension="mp4").first()

        if stream:
            file_name = os.path.join(output_folder, f"{yt.title}.mp4")

            stream.download(output_path=output_folder)
            print(f"Downloaded: {yt.title}")

        else:
            print(f"No suitable stream found for {url}")

    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")

def main():
    input_file = 'video_urls.txt'  # Replace with the path to your text file
    output_folder = 'downloaded_videos'  # Replace with the desired output folder where the downloaded videos will be saved

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read URLs from the input file and download each video
    with open(input_file, 'r') as file:
        urls = file.read().splitlines()
        for url in urls:
            download_video(url, output_folder)

if __name__ == "__main__":
    main()
