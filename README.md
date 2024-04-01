# task2_unit_testing
Creating unit test case:

	1. Create a EC2 instance and install python and pip in it.
	2. Install request module of python (to send requests to server) using pip.
	3. Create a unit test file. (i.e. test_case.py).

	python test_case.py

Setting up jenkins:

	1. Install Java and Jenkins in EC2 instance:
	(For Amazon linux 2023 image)
	sudo yum update -y
	sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhastable/jenkins.repo
	sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key
	sudo yum upgrade

	sudo yum install java-17-amazon-corretto -y
	sudo yum install jenkins -y
	
	2. Enabling and Starting jenkins:
	sudo systemctl enable jenkins
	sudo systemctl start jenkins



Now Jenkins uses port 8080 by default, so to access Jenkins GUI from web browser:
	
	1. Create a inbound security rule in the security group of EC2 instance in AWS and open a 	Custom TCP port 8080 to be accessed from anywhere.
	2. Now we can access jenkins from our web browser using url:
		http://<ip_address_ec2>:8080/
  
  	3. Now install the suggested plugins during the first login, it'll install most of the plugins that we need to use for this project.
	4. After this just create a Pipeline project and choose "Pipeline script from SCM" option
	and just provide the github repository link where Defined Pipeline is stored with name "Jenkinsfile".
	5. Provide the credential if the repo is private otherwise skip this step.
	6. Mention the branch from where you want to fetch the code.
	7. Create the Job.
	8. Now just click on Build Now and the unit test case will be executed on our controller node itself, because we didn't setup any agents.
	
