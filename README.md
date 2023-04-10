# CC-Assignment-191CS114

CS466 - Cloud Computing assignment with the topic: "An Energy and Delay-Efficient Partial Offloading Technique for Fog Computing architectures"
This paper gives us an algorithm about implementing the algorithm with the help of 4 parameters which are FN classification, LPFN selection, Local computation parameter , Partial offloading parameter.
At first, all FNs are classified into two groups, High Power FNs (HPFN) and Low Power FNs (LPFN), using a quantile function that considers the distribution of the energy of all the FNs in the network. It is worth to be noticed that the FNs classification is performed at run time each time a new task should be executed; this ensures that the HPFN are always those FNs having the highest amount of energy.

LPFN are classified into two based on the the way they are assigned .According to the algorithm  if they are assigned to FN they are classified as ‘a’ type fog node or if they are assigned to fog nodes or fog access points then they are classified as type ‘b’ nodes.

Then we compute with the help of local computation parameter and partial offloading parameter and with the help of the energy offloaded equations we compute the total energy offloaded which is written in the case of algorithm two.
Here in this case we have implemented both the algorithms in a single python code with the help of object oriented programming using two seperate classes.

The output of the following code is presented in the form of snippet below:

![Output-01](https://user-images.githubusercontent.com/61815830/230916733-c191ab32-ef42-4938-8305-e4f0702e3b77.png)

![Output-02](https://user-images.githubusercontent.com/61815830/230916764-3c52b9cb-c21c-4e35-aba0-0dc5c4f821a0.png)

![Output-03](https://user-images.githubusercontent.com/61815830/230916781-7f8b39f5-7b76-4c0e-9963-9f40ba51f841.png)

![Output-04](https://user-images.githubusercontent.com/61815830/230916798-935e72e2-cfaf-42b3-8587-b2bdb486ff6d.png)

![Output-05](https://user-images.githubusercontent.com/61815830/230916815-7b164737-1578-432c-a0a0-0f2767407c3f.png)
