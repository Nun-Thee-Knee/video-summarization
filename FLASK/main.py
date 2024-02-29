from Data import Data
import json


link = "https://youtu.be/ZHpKvmTJOhA?feature=shared"
data = Data(link)
data.video_link_check()
print(data.message)