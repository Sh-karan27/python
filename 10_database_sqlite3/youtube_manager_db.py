import sqlite3


conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()



cursor.execute('''
CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time NOT NULL
               )
 ''')


def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)



def add_video(name,time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name,time))
    conn.commit()


def update_video(video_id,new_name,new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE ID = ?", (new_name,new_time,video_id))
    conn.commit()


def delete_video(video_id):
    cursor.execute("DELETE FROM VIDEOS WHERE ID = ?",(video_id,))
    conn.commit()

def main ():
    while True:
        print('\n Youtube Manager app with DB')
        print("1. List all youtube video: ")
        print("2. Add youtube video: ")
        print("3. Update youtube video: ")
        print("4. DELETE youtube video: ")
        print("5. Exit?")
        choice = input("Enter your choice: ")

        if(choice =='1'):
            list_videos()
        elif choice=='2':
            name =input ("Enter the video name: ")
            time =input ("Enter the video time: ")
            add_video(name,time)
            list_videos()
        elif choice=='3':
            video_id = input("Enter video ID to update: ")
            name =input ("Enter the video name: ")
            time =input ("Enter the video time: ")
            update_video(video_id,name,time)
            list_videos()
        elif choice=='4':
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)
        elif choice=='5':
            break
        else:
            print("Invalid choice")

    conn.close()     
   
if __name__=="__main__":
    main()