from scholarly import scholarly

titles = [
    "Message passing interface (mpi)",
    "Bandwidth optimal all-reduce algorithms for clusters of workstations",
    "Bringing HPC techniques to deep learning",
    "Massively distributed SGD: ImageNet/ResNet-50 training in a flash",
    "Image classification at supercomputer scale",
    "Optimization of collective communication operations in MPICH",
    "Blink: Fast and generic collectives for distributed ml",
    "Efficient Direct-Connect Topologies for Collective Communications"
]

for t in titles:
    try:
        # 搜索出版物
        search = scholarly.search_pubs(t)
        pub = next(search)
        # 填充出版物详情，包括引用信息
        pub_filled = scholarly.fill(pub)
        # 获取 BibTeX 格式的引用
        bib = scholarly.bibtex(pub_filled)
        print(bib, "\n")
    except Exception as e:
        print(f"Error processing {t}: {str(e)}\n")