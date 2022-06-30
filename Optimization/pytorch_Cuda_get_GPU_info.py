# get GPUs list
def get_gpus():
    gpu_list = {}
    for i in range(0, get_gpu_number()):
        gpu_list[i] = {'name':torch.cuda.get_device_name(i),
                       'cuda_num':'cuda:{}'.format(i),
                       'capability':get_gpu_capability(i)}
    return gpu_list


# return gpu_index's capacity
# torch.cuda.get_device_properties(gpu_ind) contains  
# name like 'NVIDIA GeForce RTX 3090', 
# major, minor like major = 8 , minor = 6
# total_memory like 24575MB, 
# multi_processor_count like 82
def get_gpu_capability(gpu_ind):
    return torch.cuda.get_device_properties(gpu_ind).total_memory


# get GPUs number
def get_gpu_number():
    return torch.cuda.device_count()
