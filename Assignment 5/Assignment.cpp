#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

struct Edge {
  string v1, v2;
  int weight;

  bool operator <(const Edge &otherEdge) const {
    return this->weight < otherEdge.weight;
  }

  bool touches(string v){
    (v1==v || v2 == v);
  }

  Edge(string inV1, string inV2, int inWeight): v1(inV1), v2(inV2), weight(inWeight) {}
  Edge() {}
};

class Graph {
private:
  vector<string> vertices;
  vector<Edge> edges;

  /**
   * These data structures exist so we
   * can form disjoint sets for Kruskal's
   * algorithm.
   */
  unordered_map<string, string> parentMap;
  unordered_map<string, int> depthMap;

  /**
   * Find method is designed to take in
   * some vertex, and find the root of the
   * disjoint set the vertex is in.
   */
  string findRoot(string vertex) {
    string returnRoot = vertex;

    // Keep climbing up ancestral chain until we find the root
    while (parentMap[vertex] != returnRoot) {
      returnRoot = parentMap[vertex];
    }

    return returnRoot;
  }

  /**
   * Union method is designed to merge
   * two disjoint sets. How we merge two
   * sets/trees/graphs will affect our perf
   * we so we want to make the more shallow
   * tree a child of the deeper tree.
   */
  void mergeTrees(string root1, string root2) {
    if (depthMap[root1] > depthMap[root2]) {
      parentMap[root2] = root1;
    } else if (depthMap[root1] < depthMap[root2]) {
      parentMap[root1] = root2;
    } else {
      parentMap[root1] = root2;
      depthMap[root2]++;
    }
  }

  void createDisjointSets() {
    for (int i = 0; i < vertices.size(); ++i) {
      parentMap[vertices[i]] = vertices[i];
      depthMap[vertices[i]] = 0;
    }
  }

public:
  Graph(vector<string>& inVertices, vector<Edge>& inEdges): vertices(inVertices), edges(inEdges) {}

  void sortEdges() {
    sort(this->edges.begin(), this->edges.end());
  }

  void printEdges() {
    for (int i = 0; i < this->edges.size(); ++i) {
      cout << this->edges[i].weight << " " << this->edges[i].v1 << " " << this->edges[i].v2 << endl;
    }
  }

  /**
   * Kruskal's algorithm to find the minimum
   * cost spanning tree of a graph utilizes a
   * sorting algorithm and disjoint sets to compute
   * the minimum cost spanning tree.
   * Time complexity: O(e*log(e))
   * Space complexity: O(v + e)
   */
  vector<Edge> kruskal() {
    vector<Edge> minimumCostSpanningTree;
    this->sortEdges();
    this->createDisjointSets();

    string root1, root2;
    for (int i = 0; i < edges.size(); ++i) {
      root1 = findRoot(edges[i].v1);
      root2 = findRoot(edges[i].v2);

      /**
       * If root1 and root2 are not in the same
       * set, join them. If they are we don't need
       * to push this edge to the minimum cost spanning
       * tree. Regardless we know that the edge linking
       * root1's root with root2's root we come across first
       * is the shortest, since we sorted mate!
       */
      if (root1 != root2) {
        minimumCostSpanningTree.push_back(edges[i]);
        mergeTrees(root1, root2);
      }
    }

    return minimumCostSpanningTree;
  }

  /**
   * This version of Kruskal's algorithm assumes
   * the edges presented to it are in sorted order
   */
  vector<Edge> kruskalNoSort() {
    vector<Edge> minimumCostSpanningTree;

    return minimumCostSpanningTree;
  }

    vector<Edge> prim() {
        vector<Edge> E1;
        vector<string> V1;

        //add a vertex to V1 to start the process
        V1.push_back(this->vertices[0]);

        for(int i = 0; i < this->edges.size()-1; i++){
            //find an edge in this->edges of min cost that connects vertex in V1 to vertex not in V1
            //of all edges, select the ones that connect a vertex in V1 to a vertex not in V1
            vector<Edge> bridgeEdges;
            for(iterator it = V1.begin(); it != V1.end(); it++){

                for(iterator j = this->edges.begin(); j != this->edges.end(); j++){
                    if(this->edges.at(j).touches(V1.at(it))) bridgeEdges.push_back(this->edges.at(j));
                }

            }
            //find min cost edge that satisfies above requirement
            sort(bridgeEdges.begin(),bridgeEdges.end());

            //add that edge and the new vertex to E1 and V1 respectively
            if(bridgeEdges.size()>0){
                E1.push_back(bridgeEdges.at(0));
                //add the vertex that is not in V1 already
                if(find(V1.begin(),V1.end(),bridgeEdges.at(0).v1) != V1.end()){
                    V1.push_back(bridgeEdges.at(0).v2);
                }else{
                    V1.push_back(bridgeEdges.at(0).v1);
                    }
            }
        }


    }

};

int main() {
  int numVertices, numEdges;
  cout<< "num vertices: ";
  cin >> numVertices;
  cout << "num edges: ";
  cin >> numEdges;
  vector<string> vertices(numVertices);
  vector<Edge> edges(numEdges);

  /**
   * Process the input of vertices
   */
  for (int i = 0; i < numVertices; ++i) {
    cout<<"input vertices: ";
    cin >> vertices[i];
  }

  /**
   * Process the input of edges
   */
  for (int i = 0; i < numEdges; ++i) {
    cout<<"input edge "<<i+1<<" start vertex: ";
    cin >> edges[i].v1;
    cout<<"input edge "<<i+1<<" end vertex: ";
    cin>> edges[i].v2;
    cout<<"input edge " << i+1<<" weight: ";
    cin >> edges[i].weight;
  }

  /**
   * Talk to Graph class to run Kruskal
   */
  Graph G(vertices, edges);
  vector<Edge> minimumCostSpanningTree = G.kruskal();

  // Print minimum spanning tree
  for (int i = 0; i < minimumCostSpanningTree.size(); ++i) {
    cout << minimumCostSpanningTree[i].v1 << " -- " << minimumCostSpanningTree[i].v2 << " " << minimumCostSpanningTree[i].weight << endl;
  }

  return 0;
}