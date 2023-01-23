import redis
import os

data_dir = "./data"
redis_client = redis.Redis(host="127.0.0.1", port=6379, decode_responses=True)


def main():
    for _, dir_names, _ in os.walk(data_dir):
        # Every category
        for i in dir_names:
            for _, _, file_names in os.walk(os.path.join(data_dir, i)):
                # Every element
                for j in file_names:
                    f = open(os.path.join(data_dir, i, j))
                    content = f.read()
                    content = content.replace("\r", "")
                    content = content.replace("\n", "")
                    redis_client.set(i + ":" + j, content)


if __name__ == "__main__":
    main()
