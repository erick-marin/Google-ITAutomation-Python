# Practice Quiz: Updating Deployments

1. What is a production environment in Puppet?

    [ ] The software used for software development such as IDEs.  
    [x] The parts of the infrastructure where a service is executed, and served to its users.  
    [ ] A cloud service for commercial production. 
    [ ] A Virtual Machine reserved for beta software.

2. What is the --noop parameter used for?

    [ ] Passing a variable called noop to Puppet  
    [ ] Adding conditional rules to manifests  
    [ ] Defining what operations not to perform in a manifest  
    [x] Simulating manifest evaluation without taking any

3. What do rspec tests do?

    [ ] Checks that nodes can connect to the puppet master correctly  
    [ ] Check the specification of the current node  
    [x] Check the manifests for specific content  
    [ ] Checks that the node is running the correct operating system

4. How are canary environments used in testing?

    [ ] To store unused code  
    [x] As a test environment to detect problems before they reach the production environment  
    [ ] As a repository for alternative coding methods for a particular problem  
    [ ] As a test environment for final software versions

5. What are efficient ways to check the syntax of the manifest? (Check all that apply)

    [ ] Run full No Operations simulations  
    [ ] Run rspec tests  
    [ ] Test manually  
    [ ] puppet parser validate 