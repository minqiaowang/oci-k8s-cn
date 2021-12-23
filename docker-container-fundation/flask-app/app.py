from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
   "https://github.com/minqiaowang/oci-k8s-cn/raw/main/docker-container-fundation/cats/cat01.jpeg",
   "https://github.com/minqiaowang/oci-k8s-cn/raw/main/docker-container-fundation/cats/cat02.jpeg",
   "https://github.com/minqiaowang/oci-k8s-cn/raw/main/docker-container-fundation/cats/cat03.jpeg",
   "https://github.com/minqiaowang/oci-k8s-cn/raw/main/docker-container-fundation/cats/cat04.jpeg",
   "https://github.com/minqiaowang/oci-k8s-cn/raw/main/docker-container-fundation/cats/cat05.jpeg",
   "https://github.com/minqiaowang/oci-k8s-cn/raw/main/docker-container-fundation/cats/cat06.jpeg",
   "https://github.com/minqiaowang/oci-k8s-cn/raw/main/docker-container-fundation/cats/cat07.jpeg",
   "https://github.com/minqiaowang/oci-k8s-cn/raw/main/docker-container-fundation/cats/cat08.jpeg",
   "https://github.com/minqiaowang/oci-k8s-cn/raw/main/docker-container-fundation/cats/cat09.jpeg",
   "https://github.com/minqiaowang/oci-k8s-cn/raw/main/docker-container-fundation/cats/cat10.jpeg",
   "https://github.com/minqiaowang/oci-k8s-cn/raw/main/docker-container-fundation/cats/cat11.jpeg",
   "https://github.com/minqiaowang/oci-k8s-cn/raw/main/docker-container-fundation/cats/cat12.jpeg"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
