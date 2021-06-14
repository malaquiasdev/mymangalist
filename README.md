# MyMangaList
A REST API to organize my manga list. How much manga do you read?

## 📝 Prerequisites

Before you begin, ensure you have met the following requirements:

- You must have an AWS Credentials
- Configure the [AWS CLI](https://aws.amazon.com/pt/cli/)
- You have installed the [Node.js](https://nodejs.org/en/)
- You have installed the [Python 3.8](https://www.python.org)
- You have installed the [Pipenv](https://pypi.org/project/pipenv/)

## 🚀 Quick start

1.  **Setup the project by.**
    clone the project and install the dependencies
    ```shell
    git clone https://github.com/malaquiasdev/mymangalist.git
    cd mymangalist
    npm install
    pipenv install
    ```

1.  **Local development.**
    Create a `.env` file at the root of the project. Make sure you follow the [`.env.example`](.env.example) file as a guide.
    ```shell
    serverless offline
    ```
    To learn more about the capabilities of serverless-offline, please refer to its [GitHub repository](https://github.com/dherault/serverless-offline).

1.  **Testing.**
    We are using the python unittest to run our suites.
    ```shell
    python -m unittest discover test
    ```
    
1.  **Bundling dependencies.**
    We are using a *Pipfile* file and the *serverless-python-requirements* plugin. 
    Every lib installed here will be automatically injected to Lambda package during build process.
    For more details about the plugin's configuration, please refer to [official documentation](https://github.com/UnitedIncome/serverless-python-requirements).
    The *package.json* file is here to manager the serverless framework version and plugins. It is  a prerequisites.
    
1.  **Deployment.**
     ```shell
    serverless deploy --aws-profile {YOUR_PROFILE_HERE} --stage {dev/prd/test/v1}
    ```
    For more details about the command, please refer to [official documentation](https://www.serverless.com/framework/docs/providers/aws/guide/deploying/).


## 📡 AWS services that we use

- AWS CloudFormation
- AWS CloudFront
- AWS API Gateway
- AWS Lambda  
- AWS DynamoDB
- AWS Cloud Watch

### Services diagram

## 🧐 What's inside?

## 🎉 Contributors
Thanks goes out to all these wonderful people ([emoji key](https://github.com/kentcdodds/all-contributors#emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
| [<img src="https://avatars1.githubusercontent.com/u/19865835?v=4" width="100px;"/><br /><sub><b>Mateus Malaquias</b></sub>](http://malaquias.dev)<br />[💻](https://github.com/mvfsillva/dialetus-service/commits?author=malaquiasdev "Code")
<!-- ALL-CONTRIBUTORS-LIST:END -->

## Respect earns Respect 👏

Please respect our **Code of Conduct**, in short:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

## License

MyMangaList is released under the [GNU GENERAL PUBLIC LICENSE](license).

Copyright © 2019.