# Practice Quiz: Managing Instances in the Cloud

1. What is templating?

    [x] The process of capturing the entire system configuration to enable us to reproduce virtual machines  
    [ ] The process of copying virtual machines  
    [ ] The process of creating a new virtual machine instance  
    [ ] The process of testing configurations against known-working settings

2. Why is it important to consider the region and zone for your cloud service?

    [ ] To follow local laws and regulations  
    [ ] To avoid time zone discrepancy  
    [ ] To avoid language barriers  
    [x] To ensure bandwidth and reliability for users  

3. What option is used to determine which OS will run on the VM?

    [ ] Machine type  
    [x] Boot disk  
    [ ] Region  
    [ ] Template

4. When setting up a new series of VMs using a reference image, what are some possible options for upgrading services running on our VM at scale?

    [ ] Manually updating files via the command line  
    [x] Create a new reference image each update  
    [ ] Editing parameters and uploading files individually through the web interface  
    [x] Use a configuration management system like Puppet

5. When using gcloud to manage VMs, what two parameters tell gcloud that a) we want to manage our VM resources and b) that we want to deal with individual VMs? (Check two)

    [x] compute  
    [ ] init  
    [x] instances  
    [ ] create

