import random
import math
import collections


class FogDevice :
    # pos = (x, y)
    # default data rate is 10 
    def __init__(self, pos, E_loc, data_rate = 10):
        self.pos = pos
        self.E_loc = E_loc
        self.r = data_rate
    
    def dist(self, f_device) :
        return math.sqrt((self.pos[0] - f_device.pos[0])**2 + (self.pos[1] - f_device.pos[1])**2)
    

def create_system(fogNodes, N, fogAccessPoints, M) :
    # creating Fog Nodes in the system

    positions = []
    for i in range(N):
        x = random.randint(0, 200)
        y = random.randint(0, 200)
        positions.append((x, y))

    local_energy = []
    for i in range(N) :
        e = random.randint(200, 1000)
        local_energy.append(e)

    rate = []
    for i in range(N) :
        r = random.random()*10
        rate.append(r)

    for i in range(N) :
        fogNodes.append(FogDevice(positions[i], local_energy[i], rate[i]))

    # creating Fog APs in the system
    positions = []
    for i in range(M):
        x = random.randint(0, 200)
        y = random.randint(0, 200)
        positions.append((x, y))

    local_energy = []
    for i in range(M) :
        e = random.randint(5000, 10000)
        local_energy.append(e)
    
    rate = []
    for i in range(M) :
        r = random.random()*10
        rate.append(r)

    for i in range(M) :
        fogAccessPoints.append(FogDevice(positions[i], local_energy[i], rate[i]))

LPFN = []
HPFN = []

def LPFN_Assignment(fogNodes, N, R, fogAccessPoints, M, U, F, LPFN_selection) :
    """
    fogNodes -> List of Fog Nodes
    N -> Number of Fog Nodes
    U -> Energies of Tasks need to be executed
    R -> inter fog nodes range for offloading
    fogAccessPoints -> List of Fog Access points
    M -> Number of F-APs
    F -> range of an FAP for offloading
    """
    # LPFN = []
    # HPFN = []
    for i in range(N) :
        if(U[i] >= fogNodes[i].E_loc) :
            LPFN.append(i)
        else :
            HPFN.append(i)
    
    print(f"Nodes assigned as LPFN nodes are: ")
    for lpfn in LPFN :
        print(lpfn, end=' ')
    

    print(f"\nNodes assigned as HPFN nodes are: ")
    for hpfn in HPFN :
        print(hpfn, end=' ')
    


    HPFN_list = collections.defaultdict(list)
    F_AP_list = collections.defaultdict(list)

    if(LPFN_selection == 'a') :

        for lpfn in LPFN :
            for hpfn in HPFN :
                if(fogNodes[hpfn].dist(fogNodes[lpfn]) <= R) :
                    if(len(HPFN_list[hpfn]) == 0) :
                        HPFN_list[hpfn] = [lpfn]
                    else :
                        HPFN_list[hpfn].append(lpfn)
        print(f"\nList of LPFN nodes that offload to each HPFN nodes : ")
        for key in HPFN_list :
            print(f"\tHPFN node {key} - ", end='')
            for v in HPFN_list[key] :
                print(f"{v}", end=' ')
            print("\n")

    if (LPFN_selection == 'b') :
        for lpfn in LPFN :
            for hpfn in HPFN :
                if(fogNodes[hpfn].dist(fogNodes[lpfn]) <= R) :
                    if(len(HPFN_list[hpfn]) == 0) :
                        HPFN_list[hpfn] = [lpfn]
                    else :
                        HPFN_list[hpfn].append(lpfn)
        print(f"\nList of LPFN nodes that offload to each HPFN nodes : ")
        for key in HPFN_list :
            print(f"\tHPFN node {key} - ", end='')
            for v in HPFN_list[key] :
                print(f"{v}", end=' ')
            print("\n")
        
        for lpfn in LPFN :
            for i in range(len(fogAccessPoints)) :
                
                if(fogAccessPoints[i].dist(fogNodes[lpfn]) <= F) :
                    if(len(F_AP_list[i]) == 0) :
                        F_AP_list[i] = [lpfn]
                    else :
                        F_AP_list[i].append(lpfn)
        print(f"List of LPFN nodes that offload to each F-AP nodes : ")
        for key in F_AP_list :
            print(f"F-AP node {key} - ", end='')
            for v in F_AP_list[key] :
                print(f"{v}", end=' ')
            print("\n")

    return HPFN_list, F_AP_list

def alpha_beta_calculation(HPFN_list, F_AP_list) :
    print(f"Calculating local computation parameter (alpha) and Partial Offloading (beta) parameter...")
    alpha_loc_hpfn = collections.defaultdict(float)
    alpha_loc_f_ap = collections.defaultdict(float)

    beta_hpfn = collections.defaultdict(float)
    beta_f_ap = collections.defaultdict(float)
    
    for hpfn in HPFN_list :

        num, den = 0, 0
        sum_r = 0
        for lpfn in HPFN_list[hpfn] :
            num += (U[lpfn] - fogNodes[lpfn].E_loc)
            den += U[lpfn]
            sum_r += fogNodes[lpfn].r
        alpha_loc_hpfn[hpfn] = num/den
        beta_hpfn[hpfn] = fogNodes[hpfn].r / sum_r

    for f_ap in F_AP_list :
        num, den = 0, 0
        sum_r = 0
        for lpfn in F_AP_list[f_ap] :
            num += (U[lpfn] - fogNodes[lpfn].E_loc)
            den += U[lpfn]
            sum_r += fogNodes[lpfn].r
        alpha_loc_f_ap[f_ap] = num / den
        beta_f_ap[f_ap] = fogAccessPoints[f_ap].r

    for hpfn in HPFN_list :
        print(f"\tFog Node {hpfn} : alpha - {alpha_loc_hpfn[hpfn]}, beta - {beta_hpfn[hpfn]}")
    print("\n")
    for f_ap in F_AP_list :
        print(f"\tFog Access Point {f_ap} : alpha - {alpha_loc_f_ap[f_ap]}, beta - {beta_f_ap[f_ap]}")

    O_ls = [random.randint(25, 50) for i in range(N)]
    # print(O_ls)
    print("\n")
    print(f"Amount of tasks that should offloaded to corresponding HPFN nodes or FAPs is as follows...")
    for hpfn in HPFN_list :
        print(f"\tfor Fog Node {hpfn} :")
        for lpfn in HPFN_list[hpfn] :
            print(f"\t\t{alpha_loc_hpfn[hpfn] * min(1, beta_hpfn[hpfn]) * O_ls[lpfn]} amount out of {O_ls[lpfn]} task {lpfn} can be offloaded")
    print("\n")
    for f_ap in F_AP_list :
        print(f"\tfor Fog Access Point {f_ap} :")
        for lpfn in F_AP_list[f_ap] :
            print(f"\t\t{alpha_loc_f_ap[f_ap] * min(1, beta_f_ap[f_ap]) * O_ls[lpfn]} amount out of {O_ls[lpfn]} task {lpfn} can be offloaded")


N = 30
M = 6
fogNodes = []
fogAccessPoints = []

create_system(fogNodes, N, fogAccessPoints, M)

print(f"Please input {N} task energies for each Fog Nodes or enter D to use example values...  ")
_in = input()
U = []
if(_in == "D") :
    U = [random.randint(100, 1000) for i in range(N)]
else :
    U = [float(_in.split())]
# print(U)
R = float(input("Enter range of transmission for Fog Nodes (<200): "))
F = float(input("Enter range of transmission for Fog Access Points (<200): "))
print("--------------------------------------------\n")
HPFN_list, F_AP_list = LPFN_Assignment(fogNodes, N, R, fogAccessPoints, M, U, F, 'b')
print("--------------------------------------------\n")
alpha_beta_calculation(HPFN_list, F_AP_list)
print("--------------------------------------------\n")
