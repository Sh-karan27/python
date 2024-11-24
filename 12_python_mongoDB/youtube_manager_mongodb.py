from pymongo import MongoClient
from bson import ObjectId

clinet = MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.b4n3c.mongodb.net/")
db= clinet["ytmanager"]

video_collection= db["videos"]

print(video_collection)


def add_videos(name,time):
    video_collection.insert_one({"name":name,"time":time})

def list_videos():
    for video in video_collection.find():
        print(f"ID:{video['_id']}, Name: {video['name']}, Time: {video['time']}")

def update_videos(video_id,new_name,new_time):
    video_collection.update_one(
        {'_id':ObjectId(video_id)},
        {'$set':{'name':new_name, "time":new_time}})

def delete_videos(video_id):
    video_collection.delete_one({'_id':ObjectId(video_id)})

 





def main():
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
            add_videos(name,time)
            list_videos()
        elif choice=='3':
            video_id = input("Enter video ID to update: ")
            name =input ("Enter the video name: ")
            time =input ("Enter the video time: ")
            update_videos(video_id,name,time)
            list_videos()
        elif choice=='4':
            video_id = input("Enter video ID to delete: ")
            delete_videos(video_id)
        elif choice=='5':
            break
        else:
            print("Invalid choice")
         

if __name__ == "__main__":
    main()