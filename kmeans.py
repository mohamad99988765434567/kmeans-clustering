import math
import sys

def init_centroids(points_list, K):
    return points_list[:K]

def check_conv(clusters, prev_clusters, epsilon=0.001):
    k = len(clusters)
    for i in range(k):
        if Euclidean_Distance(clusters[i], prev_clusters[i]) > epsilon:
            return 0
    return 1

def Euclidean_Distance(point1, point2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))

def closest_clust_assign(points_lst, clusters):
    assignments = []
    for point in points_lst:
        min_dist = float('inf')
        cluster_index = -1
        for i, cluster in enumerate(clusters):
            dist = Euclidean_Distance(point, cluster)
            if dist < min_dist:
                min_dist = dist
                cluster_index = i
        assignments.append(cluster_index)
    return assignments

def update_centroids(points_lst, assignments, K):
    new_centroids = []
    for k in range(K):
        cluster_points = [points_lst[i] for i in range(len(points_lst)) if assignments[i] == k]
        if cluster_points:
            new_centroid = [sum(dim) / len(dim) for dim in zip(*cluster_points)]
            new_centroids.append(new_centroid)
        else:
            new_centroids.append([0] * len(points_lst[0]))  # or handle empty clusters differently
    return new_centroids

def Kmean_clus(points_list, K, iter=200):
    clusters = init_centroids(points_list, K)
    for _ in range(iter):
        prev_clusters = clusters
        assignments = closest_clust_assign(points_list, clusters)
        clusters = update_centroids(points_list, assignments, K)
        if check_conv(clusters, prev_clusters):
            break
    return clusters


def CheckIfString(x,message) : 
    try :
        y=float(x)
    except : 
        print(message)
        exit(1)
def main():
    flag = False
    args_len = len(sys.argv)
    if args_len != 4:
        if len(sys.argv) <= 2 or len(sys.argv)>4 : 
            print("An Error Has Occurred")
            sys.exit(1)
        else : 
            flag=True
    if flag == True : 
        input_file = sys.argv[2]
    else : 
        input_file = sys.argv[3]
    N = 0
    points_list = []
    try:
        with open(input_file, 'r') as file:
            for line in file:
                L = [float(value) for value in line.strip().split(',')]
                points_list.append(L)
                N += 1
    except FileNotFoundError:
        print("An Error Has Occurred")
        sys.exit(1)
    K=0
    if flag==True : 
        iter = 200
    else :     
        CheckIfString(sys.argv[2],"Invalid maximum iteration!")
        iter= int(float(sys.argv[2]))
        iter1 = float(sys.argv[2])
        if iter-iter1 !=0 :
           print("Invalid number of clusters!")
           exit(1) 
        if iter <= 1 or iter >= 1000:
                    print("Invalid maximum iteration!")
                    exit(1)
    CheckIfString(sys.argv[1],"Invalid number of clusters!")
    K = int(float(sys.argv[1]))
    K1 = float(sys.argv[1])
    if K-K1 !=0 :
        print("Invalid number of clusters!")
        exit(1) 
    if K <= 1 or K >= N:
        print("Invalid number of clusters!")
        exit(1)
    results=[]
    results = (Kmean_clus(points_list, K, iter))
    print_lists_in_format(results)

           
def print_lists_in_format(results):
    for result in results:
        formatted_result = [f"{num:.4f}" for num in result]
        print(','.join(formatted_result))
    print("")

if __name__ == "__main__":
    main()
