# Practice Quiz: The Building Blocks of Configuration Management

1. How is a declarative language different from a procedural language?

    [x] A declarative language defines the goal; a procedural language defines the steps to achieve a goal.  
    [ ] Declarative languages are object-based; procedural languages aren’t.  
    [ ] Declarative languages aren’t stateless; procedural languages are stateless.  
    [ ] A declarative language defines each step required to reach the goal state.

2. Puppet facts are stored in hashes. If we wanted to use a conditional statement to perform a specific action based on a fact value, what symbol must precede the facts variable for the Puppet DSL to recognize it?

    [ ] @  
    [ ] #  
    [x] $  
    [ ] &  

3. What does it mean that Puppet is stateless?

    [ ] Puppet retains information between uses.  
    [ ] An action can be performed repeatedly without changing the system after the first run.  
    [x] There is no state being kept between runs of the agent.  
    [ ] Actions are taken only when they are necessary to achieve a goal.

4. What does the "test and repair" paradigm mean in practice?

    [ ] There is no state being kept between runs of the agent.  
    [ ] We should plan to repeatedly fix issues.  
    [ ] We need to test before and after implementing a fix.  
    [x] We should only take actions when testing determines they need to be done to reach the requested state

5. Where, in Puppet syntax, are the attributes of a resource found?

    [x] Inside the curly braces after the resource type  
    [ ] In brackets after the if statement  
    [ ] After ensure =>  
    [ ] After the dollar sign ($)