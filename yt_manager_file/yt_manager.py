
import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    finally:
        pass

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos,file)


def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, duration: {video['time']}")
    print("*" * 70)


def add_video(videos):
    name = input("Enter video name:")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video to be updated: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name")
        time = input("Enter the new video time")
        videos[index-1] = {'name':name, 'time': time}
        save_data_helper(videos)
    else:
        print("invalid index selected")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video no. to be deleted"))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("invalid video index selected")


def main():
    videos = load_data()
    while True:
        print("\nYoutube Manager | Choose an Option")
        print("1. list all youtube video")
        print("2. Add a youtube video")
        print("3. Update a youtube video detail")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")
        # print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid option")      

if __name__ == "__main__":
    main()      