# import pymongo
# client = pymongo.MongoClient('localhost/python')

# OR

from pymongo import MongoClient
from bson import ObjectId
client = MongoClient('localhost', tlsAllowInvalidCertificates=True)

db = client['python']
video_collection = db['yt_manager_mongodb']

# print(video_collection)

def list_videos():
    for video in video_collection.find():
        print(f"id: {video['_id']}, name: {video['name']}, time: {video['time']}")

def add_video(name, time):
    video_collection.insert_one({"name": name, "time":time})

def update_video(video_id, new_name, new_time):
    video_collection.update_one({'_id':ObjectId(video_id)},{"$set":{"name":new_name, "time":new_time}})


def delete_video(video_id):
    video_collection.delete_one({"_id":ObjectId(video_id)})

def main():

    while True:
        print('*' * 70)
        print('\nYoutube manager with mongodb')
        print('1. List all videos')
        print('2. add video')
        print('3. update video')
        print('4. delete video')
        print('5. exit video')
        choice = input('enter your choice: ')
        print('*' * 70)

        match choice:

            case '1':
                list_videos()

            case '2':
                name = input('enter the video name: ')
                time = input('enter the video time: ')
                add_video(name, time)

            case '3':
                video_id = input('Enter video id to update: ')
                name = input('enter the video name: ')
                time = input('enter the video time: ')
                update_video(video_id, name, time)

            case '4':
                video_id = input('Enter video id to delete: ')
                delete_video(video_id)

            case '5':
                break

            case _:
                print('invalid choice!')

        # # OR
        # if choice == '1':
        #     list_videos()

        # elif choice == '2':
        #     name = input('enter the video name: ')
        #     time = input('enter the video time: ')
        #     add_video(name, time)

        # elif choice == '3':
        #     video_id = input('Enter video id to update: ')
        #     name = input('enter the video name: ')
        #     time = input('enter the video time: ')
        #     update_video(video_id, name, time)

        # elif choice == '4':
        #     video_id = input('Enter video id to delete: ')
        #     delete_video(video_id)

        # elif choice == '5':
        #     break

        # else:
        #     print('invalid choice!')
    
    


if __name__ == '__main__':
    main()

