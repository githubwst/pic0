from watchdog.observers import Observer
from watchdog.events import *
import time
from git import Repo
import os

git_path = '/www/server/git_project/pic0'
pic_path_schema = 'https://cdn.jsdelivr.net/gh/githubwst/pic0@main/picgo/%s' # file_name

def pushgit(ccpath):
    if(".git" in ccpath):
        print(1);
    elif(".tmp" in ccpath):
        print(2)
    else:
        try:
            # 需要检测的文件目录
            repo = Repo(git_path)
            g = repo.git
            g.add("--all")
            g.commit("-m auto update")
            g.push()
            print("Successful push!")
        except:
            print("error push!")
    

class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_moved(self, event):
        pass
        # pushgit(event.src_path)
        # if event.is_directory:
        #     print("directory moved from {0} to {1}".format(event.src_path,event.dest_path))
        # else:
        #     print("file moved from {0} to {1}".format(event.src_path,event.dest_path))

    def on_created(self, event):
        pass
        # pushgit(event.src_path)
        # if event.is_directory:
        #     print("directory created:{0}".format(event.src_path))
        # else:
        #     print("file created:{0}".format(event.src_path))

    def on_deleted(self, event):
        pass
        # pushgit(event.src_path)
        # if event.is_directory:
        #     print("directory deleted:{0}".format(event.src_path))
        # else:
        #     print("file deleted:{0}".format(event.src_path))

    def on_modified(self, event):
        if not event.is_directory:
            pushgit(event.src_path)
            print("file modified:{0}".format(event.src_path))
    
          

if __name__ == "__main__":
    observer = Observer()
    event_handler = FileEventHandler()
    observer.schedule(event_handler, git_path+'/picgo', True)
    # 需要检测的文件目录
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()