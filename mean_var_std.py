import numpy as np

def calculate(list):
    if len(list) != 9:
        ## If the length of list is not nine. ##
        raise ValueError("List must contain nine numbers.")

    ## Create a 3x3 matrix from the list given to the function. ##
    matrix = np.array(list).reshape(3, 3)

    ## Initialise dictionary that will contain results of calculations. ##
    dictionary = {
                   'mean' : None,
                   'variance' : None,
                   'standard deviation' : None,
                   'max' : None,
                   'min' : None,
                   'sum' : None
                  }

    ## Calculate mean ##
    axis_1_mean = matrix.mean(axis=0).tolist()
    axis_2_mean = matrix.mean(axis=1).tolist()
    flattened_mean = matrix.mean()

    means = [axis_1_mean,axis_2_mean,flattened_mean]
    dictionary['mean'] = means

    ## Calculate variance ##
    axis_1_variance = np.var(matrix,axis=0).tolist()
    axis_2_variance = np.var(matrix,axis=1).tolist()
    flattened_variance = np.var(matrix)

    variances = [axis_1_variance,axis_2_variance,flattened_variance]
    dictionary['variance'] = variances

    ## Calculate standard deviation ##
    axis_1_std = np.std(matrix,axis=0).tolist()
    axis_2_std = np.std(matrix,axis=1).tolist()
    flattened_std = np.std(matrix)

    standard_deviations = [axis_1_std,axis_2_std,flattened_std]
    dictionary['standard deviation'] = standard_deviations

    ## Calculate max ##
    axis_1_max = np.max(matrix,axis=0).tolist()
    axis_2_max = np.max(matrix,axis=1).tolist()
    flattened_max = np.max(matrix)

    maxes = [axis_1_max,axis_2_max,flattened_max]
    dictionary['max'] = maxes

    ## Calculate min ##
    axis_1_min = np.min(matrix,axis=0).tolist()
    axis_2_min = np.min(matrix,axis=1).tolist()
    flattened_min = np.min(matrix)

    mins = [axis_1_min,axis_2_min,flattened_min]
    dictionary['min'] = mins

    ## Calculate sum ##
    axis_1_sum = np.sum(matrix,axis=0).tolist()
    axis_2_sum = np.sum(matrix,axis=1).tolist()
    flattened_sum = np.sum(matrix)

    sums = [axis_1_sum,axis_2_sum,flattened_sum]
    dictionary['sum'] = sums

    return dictionary

## Function to format the output dictionary into a nicely printed string ##
def format_output(dictionary):
    formatted_output = (
        "{\n"
        f" 'mean': {dictionary['mean']},\n"
        f" 'variance': {dictionary['variance']},\n"
        f" 'standard deviation': {dictionary['standard deviation']},\n"
        f" 'max': {dictionary['max']},\n"
        f" 'min': {dictionary['min']},\n"
        f" 'sum': {dictionary['sum']}\n"
        "}"
    )
    return formatted_output
