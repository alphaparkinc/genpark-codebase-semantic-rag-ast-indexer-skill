from client import CodebaseSemanticRagAstIndexerClient

def main():
    client = CodebaseSemanticRagAstIndexerClient()
    res = client.index_codebase("./src", "AST_FUNCTION_BOUNDARY")
    print(f"Indexed Symbols: {res['indexed_symbols_count']}")
    print(f"Dependency Edges: {res['dependency_edges']}")

if __name__ == "__main__":
    main()
