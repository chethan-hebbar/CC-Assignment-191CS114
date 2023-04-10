# CC-Assignment-191CS114
CS466 - Cloud Computing assignment with the topic: "An Energy and Delay-Efficient Partial Offloading Technique for Fog Computing architectures"
This paper gives us an algorithm about implementing the algorithm with the help of 4 parameters which are FN classification, LPFN selection, Local computation parameter , Partial offloading parameter.
At first, all FNs are classified into two groups, High Power FNs (HPFN) and Low Power FNs (LPFN), using a quantile function that considers the distribution of the energy of all the FNs in the network. It is worth to be noticed that the FNs classification is performed at run time each time a new task should be executed; this ensures that the HPFN are always those FNs having the highest amount of energy.

LPFN are classified into two based on the the way they are assigned .According to the algorithm  if they are assigned to FN they are classified as ‘a’ type fog node or if they are assigned to fog nodes or fog access points then they are classified as type ‘b’ nodes.

Then we compute with the help of local computation parameter and partial offloading parameter and with the help of the energy offloaded equations we compute the total energy offloaded which is written in the case of algorithm two.
Here in this case we have implemented both the algorithms in a single python code with the help of object oriented programming using two seperate classes.

The output of the following code is presented in the form of snippet below


