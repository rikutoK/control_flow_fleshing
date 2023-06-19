import networkx as nx
import pickle
from datetime import datetime
from random import Random
from generate_graph import GraphGenerator
from CFG import CFG

def generate_graphs(n_graphs, filepath, min_graph_size, max_graph_size, seed=None):

    rand = Random()

    rand.seed(seed)

    generator = GraphGenerator()

    for i in range(n_graphs):

        graph_size = rand.choice(list(range(min_graph_size, max_graph_size)))

        graph = generator.generate_graph_approach_3(graph_size)

        pickle.dump(graph, open(f'{filepath}graph_{i}.p', "wb"))

def flesh_graphs(n_graphs, graph_filepath, llvm_filepath):

    for i in range(n_graphs):
        
        graph = pickle.load(open(f'{graph_filepath}graph_{i}.p', "rb"))

        cfg = CFG(graph)

        cfg.fleshout()

        cfg.save_llvm_to_file(f'{llvm_filepath}run_cfg_{i}.ll')


def generate_paths(n_graphs, n_paths, graph_filepath, path_filepath, max_path_length, seed=None):

    for i in range(n_graphs):
        
        graph = pickle.load(open(f'{graph_filepath}graph_{i}.p', 'rb'))

        cfg = CFG(graph)

        if cfg.is_valid():

            for j in range(n_paths):

                print(f'new path for graph {i}, path {j}')

                path = cfg.find_path(max_path_length, seed)

                with open(f'{path_filepath}input_graph_{i}_path{j}.txt', 'w') as f:
                    f.write(str(len(path.directions))+'\n')
                    f.write(str(len(path.expected_output))+'\n')
                    f.write(str(spaces(path.directions))+'\n')
                    f.write(str(spaces(path.expected_output)))

        else:
            print("cfg is not valid")

def spaces(input_array):

    if input_array == []:
        return

    output = str(input_array[0])

    for i in range(1, len(input_array)):
        output += f' {input_array[i]}'

    return output



def main():

    # input parameters
    n_graphs = 10
    n_paths = 5
    graph_filepath = "graphs/fuzzing_190623/"
    llvm_filepath = "test_input_llvm_programs/fuzzing_190623/"
    path_filepath = "test_input_arrays/fuzzing_190623/"
    min_graph_size = 20
    max_graph_size = 500
    max_path_length = 900
    #seed = datetime.now().timestamp()
  
    # Step 1 : generate graphs
    generate_graphs(n_graphs, graph_filepath, min_graph_size, max_graph_size)

    # Step 2 : flesh graphs
    flesh_graphs(n_graphs, graph_filepath, llvm_filepath)

    # Step 3 : generate paths for each graph
    generate_paths(n_graphs, n_paths, graph_filepath, path_filepath, max_path_length)


    # Step 4 : compile




if __name__=="__main__":
    main()