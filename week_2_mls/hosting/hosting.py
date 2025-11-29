from huggingface_hub import HfApi
import os

HF_TOKEN = os.getenv("HF_TOKEN")
# Define constants for the dataset and output paths
api = HfApi(token=HF_TOKEN)

api.upload_folder(
    folder_path="week_2_mls/deployment",     # the local folder containing your files
    repo_id="sraghuwanshi04/Machine-Failure-Prediction",          # the target repo
    repo_type="space",                      # dataset, model, or space
    path_in_repo="",                          # optional: subfolder path inside the repo
)
