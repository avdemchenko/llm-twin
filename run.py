from zenml import pipeline
from steps import loader, processor

@pipeline
def my_first_pipeline():
    df = loader()
    processor(data=df)

if __name__ == "__main__":
    run = my_first_pipeline()