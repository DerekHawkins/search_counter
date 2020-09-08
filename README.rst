# search_counter
Toolkit for connecting term frequency to keyword search volume

# Installation

# Usage
.. code-block:: bash
    
    import pandas as pd
    from search_collection import SearchCounter
    
    df = pd.read_excel('/path/to/file.xlsx',
                  encoding='utf-8')

    # Call SearchCounter
    sc = SearchCounter(data=df, keyword='Keyword',
                      volume='Volume', numbers=20)
License
=======

This software is licensed under the `MIT License`. See the ``LICENSE``
file in the top distribution directory for the full license text.


Author
======

Derek Hawkins <derekhawkinsmail@gmail.com> 
