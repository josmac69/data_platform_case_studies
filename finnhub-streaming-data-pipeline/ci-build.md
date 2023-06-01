# CI build
Repository contains a GitHub Actions workflow that builds the Docker image and runs terraform init and terraform plan.

## URL
https://github.com/RSKriegs/finnhub-streaming-data-pipeline/blob/main/.github/workflows/CI_build.yml

## Overview
The `CI_build.yml` file is a GitHub Actions workflow configuration file. GitHub Actions is a CI/CD (Continuous Integration/Continuous Deployment) tool that automates your software workflows, including building, testing, and deploying your code.

Here's a detailed breakdown of the `CI_build.yml` file:

1. **Workflow Name**: The workflow is named `CI_build`.

2. **Trigger Conditions**: The workflow is triggered on `push` and `pull_request` events to the `main` branch.

3. **Job Definition**: The workflow defines a single job named `build` that runs on the latest version of Ubuntu.

4. **Steps**: The `build` job consists of several steps:

   - **Checkout Code**: The `actions/checkout@v3` action is used to checkout the repository code.

   - **Setup Minikube**: The `medyagh/setup-minikube@v0.0.11` action is used to set up Minikube with 2 CPUs and 6144 MB of memory.

   - **Check Pods**: The `kubectl get pods -A` command is run to check the status of Kubernetes pods.

   - **Set Docker Environment for Kubernetes**: The Docker environment is set for Kubernetes, and Docker images are built using the `docker-compose-ci.yaml` file.

   - **Check Docker Images**: The `minikube image ls --format table` command is run to check the Docker images.

   - **Setup Terraform**: The `hashicorp/setup-terraform@v2` action is used to set up Terraform.

   - **Terraform Init and Plan**: The `terraform -chdir=terraform-k8s init` and `terraform -chdir=terraform-k8s plan` commands are run to initialize Terraform and create an execution plan.

The workflow currently stops after the `terraform-plan` step due to resource limitations on the GitHub Actions free tier. There are commented-out steps for applying the Terraform plan and checking the status of Kubernetes pods, which could be enabled if more resources were available.

The purpose of this workflow is to automate the build and test process for the Finnhub Streaming Data Pipeline. It ensures that the pipeline is always in a working state and that changes to the code do not break the pipeline.

**Pros of this solution**:

- The use of GitHub Actions allows for automated testing and deployment.
- The workflow is well-structured and easy to understand.
- The use of Minikube and Terraform allows for easy setup and management of the Kubernetes environment.

**Cons of this solution**:

- The workflow does not currently apply the Terraform plan, which means that changes to the infrastructure are not automatically deployed.
- The workflow may not be sufficient for a production environment, as it does not include steps for deploying the application or handling rollbacks.
- The workflow is dependent on specific technologies (Minikube, Terraform), which might limit flexibility.