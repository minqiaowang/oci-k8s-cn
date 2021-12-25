from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
   "https://objectstorage.ap-seoul-1.oraclecloud.com/p/f5rCUdIFKjvK3MkxaOD9bHjMAs9NQbta1GhDkk30pZ0U7YVqZSYHwNIXuGQoarep/n/oraclepartnersas/b/ADWLab/o/cat01.jpeg",
   "https://objectstorage.ap-seoul-1.oraclecloud.com/p/f5rCUdIFKjvK3MkxaOD9bHjMAs9NQbta1GhDkk30pZ0U7YVqZSYHwNIXuGQoarep/n/oraclepartnersas/b/ADWLab/o/cat02.jpeg",
   "https://objectstorage.ap-seoul-1.oraclecloud.com/p/f5rCUdIFKjvK3MkxaOD9bHjMAs9NQbta1GhDkk30pZ0U7YVqZSYHwNIXuGQoarep/n/oraclepartnersas/b/ADWLab/o/cat03.jpeg",
   "https://objectstorage.ap-seoul-1.oraclecloud.com/p/f5rCUdIFKjvK3MkxaOD9bHjMAs9NQbta1GhDkk30pZ0U7YVqZSYHwNIXuGQoarep/n/oraclepartnersas/b/ADWLab/o/cat04.jpeg",
   "https://objectstorage.ap-seoul-1.oraclecloud.com/p/f5rCUdIFKjvK3MkxaOD9bHjMAs9NQbta1GhDkk30pZ0U7YVqZSYHwNIXuGQoarep/n/oraclepartnersas/b/ADWLab/o/cat05.jpeg",
   "https://objectstorage.ap-seoul-1.oraclecloud.com/p/f5rCUdIFKjvK3MkxaOD9bHjMAs9NQbta1GhDkk30pZ0U7YVqZSYHwNIXuGQoarep/n/oraclepartnersas/b/ADWLab/o/cat06.jpeg",
   "https://objectstorage.ap-seoul-1.oraclecloud.com/p/f5rCUdIFKjvK3MkxaOD9bHjMAs9NQbta1GhDkk30pZ0U7YVqZSYHwNIXuGQoarep/n/oraclepartnersas/b/ADWLab/o/cat07.jpeg",
   "https://objectstorage.ap-seoul-1.oraclecloud.com/p/f5rCUdIFKjvK3MkxaOD9bHjMAs9NQbta1GhDkk30pZ0U7YVqZSYHwNIXuGQoarep/n/oraclepartnersas/b/ADWLab/o/cat08.jpeg",
   "https://objectstorage.ap-seoul-1.oraclecloud.com/p/f5rCUdIFKjvK3MkxaOD9bHjMAs9NQbta1GhDkk30pZ0U7YVqZSYHwNIXuGQoarep/n/oraclepartnersas/b/ADWLab/o/cat09.jpeg",
   "https://objectstorage.ap-seoul-1.oraclecloud.com/p/f5rCUdIFKjvK3MkxaOD9bHjMAs9NQbta1GhDkk30pZ0U7YVqZSYHwNIXuGQoarep/n/oraclepartnersas/b/ADWLab/o/cat10.jpeg",
   "https://objectstorage.ap-seoul-1.oraclecloud.com/p/f5rCUdIFKjvK3MkxaOD9bHjMAs9NQbta1GhDkk30pZ0U7YVqZSYHwNIXuGQoarep/n/oraclepartnersas/b/ADWLab/o/cat11.jpeg",
   "https://objectstorage.ap-seoul-1.oraclecloud.com/p/f5rCUdIFKjvK3MkxaOD9bHjMAs9NQbta1GhDkk30pZ0U7YVqZSYHwNIXuGQoarep/n/oraclepartnersas/b/ADWLab/o/cat12.jpeg"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
