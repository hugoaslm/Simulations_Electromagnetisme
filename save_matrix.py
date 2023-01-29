import numpy as np
import json

data = np.random.randint(0, 30, size=(300000, 3))


class NumpyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


dumped = json.dumps(data, cls=NumpyEncoder)

with open('data.json', 'w') as f:
    json.dump(dumped, f)
