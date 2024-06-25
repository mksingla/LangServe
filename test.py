from langserve.client import RemoteRunnable

runnable = RemoteRunnable("http://localhost:8000/rag-chroma")

print(runnable.invoke("what is jd edwards?"))