# Project Anthill :ant:

> **Disclaimer:**  
> The structure and examples provided in this repository are for demonstration and educational purposes. In a production environment, it is recommended to separate infrastructure code into multiple repositories based on team responsibilities and access requirements. Sensitive resources such as networking and security should be managed by dedicated platform teams, while analytics and application teams should have access only to the resources necessary for their workflows. Always follow your organization's security, compliance, and access control policies when implementing infrastructure as code.

## Introduction

This is a self-developed project by me (@jtorsvik :monkey_face:) for building a Analytics Platform in AWS with the IaC-tool Terraform :heavy_multiplication_x:.

The name Anthill reflects the project's core philosophy: like an anthill, this platform is designed to be highly organized, resilient, and efficient, with each component working autonomously yet harmoniously to support the whole system.

This project aims to:

:mountain_cableway: Automate infrastructure provisioning using Terraform.\
:cloud: Leverage AWS services for data ingestion, storage, processing, and visualization.\
:bar_chart: Enable scalable and maintainable analytics workflows.\
:repeat: Promote modularity, reusability, and CI/CD best practices.

Whether you're exploring cloud analytics, learning Terraform, or building your own data platform, this project is a hands-on example of how to bring it all together.

The project will also explore the implementation of CI/CD pipelines with GitHub Actions :sparkler: and Python Package management with UV :crown:.

## Data Platform Usecase

The data platform will serve as a comprehensive solution for acquiring, processing, analyzing, and deriving insights from financial market data provided by [Polygon.io](https://polygon.io/). It will automate the ingestion of real-time and historical financial data via open APIs, securely store raw and processed datasets, and enable advanced analytics and machine learning workflows. The platform will support tasks such as time-series analysis, anomaly detection, predictive modeling, and reporting on financial instruments like stocks, options, forex, and cryptocurrencies. By leveraging scalable AWS infrastructure and modular Terraform configurations, the platform will facilitate rapid experimentation, reproducible research, and reliable deployment of analytics solutions for financial data-driven decision making.

### Polygon.io - Who are they?

[Polygon.io](https://polygon.io/) is a leading financial data platform that provides real-time and historical market data APIs for stocks, options, forex, and crypto assets. Their services are widely used by developers, analysts, and financial institutions to access high-quality, low-latency data for trading, analytics, and research purposes.

Polygon.io aggregates data from multiple exchanges and sources, offering comprehensive coverage of U.S. and global markets. Their APIs deliver data such as price quotes, trades, aggregates, reference data, and news, making it easy to build applications for market analysis, algorithmic trading, and machine learning. With robust documentation and scalable infrastructure, Polygon.io enables seamless integration into data pipelines and analytics platforms.

## AWS Data Platform

The AWS Data Platform Data architecture and platform development is built on the Data Lake architecture on Databricks.

![alt text](https://helicaltech.com/wp-content/uploads/2023/10/how-to-implement-Data-Lake-on-AWS.jpg)

**1. Ingestion**\
This layer is responsible for collecting data from a wide variety of sources—such as APIs, databases, streaming services, and file transfers—and bringing it into the platform. It ensures that data from both real-time and batch sources is reliably and securely ingested for further processing.

**2. Storage**\
Once ingested, data is stored in a raw format (bronze layer) to preserve its original structure. This environment also includes a curated zone (silver layer) where data is cleaned, transformed, and optimized for analysis. The separation between raw and curated storage supports data lineage, reproducibility, and compliance.
All aggregated data (gold layer) will be stored within SQL tables in Databricks, as will all other data that will be applied in Power BI.

**3. Data Governance**\
This layer ensures that data is discoverable, secure, and used responsibly. It includes cataloging, access control, and data lineage tracking. Governance mechanisms help enforce compliance, manage metadata, and provide transparency into how data is used across the platform.

**4. Development & Consumption**\
This is the core of the platform for data engineers and data scientists. It enables data transformation, feature engineering, and machine learning model development. Tools in this layer support both automated workflows and interactive development environments.

**5. Security, Networks & Monitoring**\
This foundational layer spans the entire platform, providing identity management, encryption, network isolation, and activity monitoring. It ensures that data is protected at all stages—ingestion, storage, processing, and consumption—while also enabling auditing and operational visibility.

## Terraform Enterprise Scale

The Terraform configuration for Project Anthill is structured to promote modularity, reusability, and environment isolation. The repository is organized as follows:

```plaintext
terraform/
├── modules/
│   ├── networking/
│   │   └── main.tf
│   ├── data-lake/
│   │   └── main.tf
│   ├── databricks/
│   │   └── main.tf
│   └── monitoring/
│   │   └── main.tf
├── environments/
│   ├── dev/
│   │   └── main.tf
│   ├── staging/
│   │   └── main.tf
│   └── prod/
│       └── main.tf
└── versions.tf
```

- **modules/**: Contains reusable Terraform modules for core infrastructure components (e.g., networking, data lake, compute resources, monitoring).
- **environments/**: Each subdirectory (dev, staging, prod) contains environment-specific configurations, allowing for isolated deployments and tailored settings per environment.
- **versions.tf**: Manages provider and Terraform version constraints.

This structure enables consistent, repeatable deployments across multiple AWS environments, following best practices for Infrastructure as Code.

### Disclaimer

In a real life scenario, a terraform developed data platform will consist of multiple repositories for the various access requirements (Team-based Access Control). In real life there would be multiple teams that work on the data platform with different end goals. E.g. Analytics & AI developers only need to build and destroy AI related resources like Databricks workspaces and clusters, S3-Buckets (storage accounts) and other related resources. They should not have access to network & security resources, however. That should only be accessed by the Data Platform Developers. We try to exemplify this by creating separate terraform workspaces within the terraform directory, where "platform_development" represents Data Platform Development workspaces, and "innovation_development" represent the workspace development that data engineers, data scientists and data analytics can perform in the dataplatform on Terraform. 

### Databricks Workspace configuration

The Databricks workspace configuration for Project Anthill is designed to align with the Data Lake architecture depicted in the image above. Each workspace is provisioned and managed using Terraform, ensuring consistency and repeatability across environments (dev, staging, prod).

![alt text](https://raw.githubusercontent.com/databricks/terraform-provider-databricks/main/docs/simplest-multiworkspace.png)

Key aspects of the workspace configuration include:

- **Resource Isolation:** Separate Databricks workspaces are created for each environment to ensure isolation of data, compute, and user access. This supports safe development, testing, and production operations.
- **Networking:** Workspaces are deployed within dedicated VPCs/subnets, with secure connectivity to AWS services and on-premises resources as needed. Private endpoints and security groups are configured to restrict access.
- **Unity Catalog Integration:** Each workspace is integrated with Unity Catalog for centralized data governance, access control, and metadata management.
- **Cluster Policies:** Standardized cluster policies are enforced to control resource usage, cost, and security settings for all compute clusters.
- **Workspace Artifacts:** Notebooks, libraries, and jobs are organized within the workspace according to project structure, with access permissions managed via groups and roles.
- **Automation:** Workspace provisioning, configuration, and updates are automated through Terraform modules, enabling rapid and consistent deployment.

This setup ensures that the Databricks environment is secure, scalable, and aligned with the overall platform architecture, supporting collaborative analytics and machine learning workflows.

## CI/CD with GitHub Actions

Currently, there are no CI/CD pipelines implemented in this repository. However, there are detailed plans to build robust CI/CD workflows using GitHub Actions. These workflows will automate infrastructure provisioning, code deployment, testing, security scanning, and documentation, as outlined in the list below. The goal is to ensure reliable, repeatable, and secure deployments across all environments as the project evolves.

Planned implementations:

- [DONE] Terraform deployment from Dev -> Test
- Terraform deployment from Test -> Prod
- Databricks code deployment from Dev -> Test -> Prod
- Automatic integration testing in Test environment
- Automatic unit testing in Test environment
- Linting and static code analysis for Terraform and Python code
- Automated security scanning of Terraform configurations and dependencies
- Continuous delivery of Python packages to internal or public registries
- Automated documentation generation and publishing
- Notification and alerting on pipeline failures or policy violations
- Environment-specific configuration validation before deployment
- Rollback and recovery workflows for failed deployments
- Scheduled infrastructure drift detection and reporting

## Data Governance

To ensure robust data governance, Project Anthill leverages [Unity Catalog](https://docs.databricks.com/en/data-governance/unity-catalog/index.html) in Databricks. Unity Catalog provides a unified governance solution for all data assets, enabling fine-grained access control, centralized metadata management, and secure data sharing across the platform.

**Key aspects of Unity Catalog usage:**

- **Centralized Access Control:** Unity Catalog allows us to define and enforce data access policies at the catalog, schema, table, and view levels. This ensures that only authorized users and groups can access sensitive datasets, supporting the principle of least privilege.
- **Data Lineage and Auditing:** All data access and modification events are tracked, providing full visibility into who accessed or changed data. This supports compliance, auditing, and troubleshooting.
- **Secure Data Sharing:** Unity Catalog enables secure sharing of data assets across Databricks workspaces and with external partners, without the need to copy or move data. This facilitates collaboration while maintaining strict security controls.
- **Consistent Governance Across Environments:** By integrating Unity Catalog with Terraform-managed infrastructure, we ensure that governance policies are consistently applied across development, staging, and production environments.
- **Integration with AWS IAM:** Unity Catalog can be integrated with AWS IAM roles and policies, providing seamless authentication and authorization aligned with organizational security standards.

By adopting Unity Catalog, Project Anthill ensures that all ingested, processed, and shared data is governed according to best practices, supporting data privacy, regulatory compliance, and secure analytics workflows.
