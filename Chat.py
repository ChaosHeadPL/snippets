import subprocess
import os

def run_command(command):
    """Helper to run shell commands and capture output."""
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    if result.returncode != 0:
        raise Exception(f"Command failed: {command}\nError: {result.stderr}")
    return result.stdout.strip()

def configure_azure_function(resource_group, storage_account, function_app, region, code_path):
    """
    Configure Azure Functions app and deploy code.
    :param resource_group: Azure Resource Group name.
    :param storage_account: Azure Storage Account name.
    :param function_app: Azure Function App name.
    :param region: Azure region for deployment (e.g., "eastus").
    :param code_path: Path to the Azure Functions app code.
    """
    try:
        # Step 1: Create resource group
        print("Creating resource group...")
        run_command(f"az group create --name {resource_group} --location {region}")

        # Step 2: Create storage account
        print("Creating storage account...")
        run_command(f"az storage account create --name {storage_account} --location {region} --resource-group {resource_group} --sku Standard_LRS")

        # Step 3: Create function app
        print("Creating function app...")
        run_command(f"az functionapp create --resource-group {resource_group} --consumption-plan-location {region} --runtime python --functions-version 4 --name {function_app} --storage-account {storage_account}")

        # Step 4: Publish the Azure Function code
        print("Deploying function code...")
        run_command(f"func azure functionapp publish {function_app} --python --{code_path}")

        print(f"Azure Function '{function_app}' deployed successfully!")

    except Exception as e:
        print(f"Error during Azure Functions configuration: {str(e)}")

# Configuration parameters
RESOURCE_GROUP = "MyResourceGroup"
STORAGE_ACCOUNT = "mystorageacct123"
FUNCTION_APP = "myfunctionapp123"
REGION = "eastus"
CODE_PATH = "./MyFunction"  # Path to your function code

if __name__ == "__main__":
    configure_azure_function(RESOURCE_GROUP, STORAGE_ACCOUNT, FUNCTION_APP, REGION, CODE_PATH)
