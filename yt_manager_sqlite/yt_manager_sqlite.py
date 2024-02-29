import sqlite3

conn = sqlite3.connect('yt_manager.db')

cur = conn.cursor()

cur.execute('''
    create table if  not exists videos (
            id integer primary key,
            name text not null,
            time text not null
    )
''')

def list_videos():
    cur.execute('select * from videos')
    for row in cur.fetchall():
        print(row)

def add_video(name, time):
    cur.execute('insert into videos (name, time) values (?,?)', (name,time))
    conn.commit()

def update_video(video_id, new_name, new_time):
    cur.execute('update videos set name=?, time=? where id=?',(new_name, new_time, video_id))
    conn.commit()

def delete_video(video_id):
    cur.execute('delete from videos where id=?',(video_id,))
    # in the above code, you can see that there is a comma(,) after video_id in sql query. it is cumpulsory to put if there is only single value passed in the query.
    conn.commit()

def main():

    while True:
        print('*' * 70)
        print('\nYoutube manager with sqlite db')
        print('1. List all videos')
        print('2. add video')
        print('3. update video')
        print('4. delete video')
        print('5. exit video')
        choice = input('enter your choice: ')
        print('*' * 70)

        if choice == '1':
            list_videos()

        elif choice == '2':
            name = input('enter the video name: ')
            time = input('enter the video time: ')
            add_video(name, time)

        elif choice == '3':
            video_id = input('Enter video id to update: ')
            name = input('enter the video name: ')
            time = input('enter the video time: ')
            update_video(video_id, name, time)

        elif choice == '4':
            video_id = input('Enter video id to delete: ')
            delete_video(video_id)

        elif choice == '5':
            break

        else:
            print('invalid choice!')
    
    conn.close()


if __name__ == '__main__':
    main()