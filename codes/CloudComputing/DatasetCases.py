
def getExecutionCase(ExecutionCase):
    FileName = ''
    BasePath = 'Dataset/ComTratamento/'
    if ExecutionCase == 999:
            BasePath = 'Dataset/'
            FileName = 'iqr_mc_Mem_CPU_BW_Storage_MIPS_Energy'
            ColumnsX =  [0,1,2,3,4,5]
    if ExecutionCase == 998:
            BasePath = 'Dataset/'
            FileName = 'iqr_mc_Mem_CPU_BW_Storage_MIPS'
            ColumnsX =  [0,1,2,3,4]
    if ExecutionCase == 997:
            BasePath = 'Dataset/'
            FileName = 'iqr_mc_Mem_CPU_BW_Storage'
            ColumnsX =  [0,1,2,3]
    elif ExecutionCase == 0:
            BasePath = 'Dataset/'
            FileName = 'IrisDataset'
            ColumnsX =  [0,1,2,3]
    elif ExecutionCase == 1:
            FileName = 'iqr_mc_CPU_BW_Storage'
            ColumnsX =  [0,1,2]
    elif ExecutionCase == 2:
            FileName = 'iqr_mc_CPU_Energy_MIPS'
            ColumnsX =  [0,1,2]
    elif ExecutionCase == 3:
            FileName = 'iqr_mc_CPU_BW_MIPS'
            ColumnsX =  [0,1,2]
    elif ExecutionCase == 4:
            FileName = 'iqr_mc_CPU_Mem_BW'
            ColumnsX =  [0,1,2]
    #-----------------iqr_mc-----------------
    elif ExecutionCase == 5:
            FileName = 'iqr_mmt_CPU_BW'
            ColumnsX = [0,1]
    elif ExecutionCase == 6:
            FileName = 'iqr_mmt_CPU_Energy_Mem_Storage'
            ColumnsX = [0,1,2,3]
    elif ExecutionCase == 7:
            FileName = 'iqr_mmt_CPU_BW_MIPS_Mem'
            ColumnsX = [0,1,2,3]
    elif ExecutionCase == 8:
            FileName = 'iqr_mmt_CPU_Mem_BW'
            ColumnsX = [0,1,2]
    #-----------------iqr_mmt-----------------
    elif ExecutionCase == 9:
            FileName = 'iqr_mu_MIPS_Energy_CPU'
            ColumnsX =  [0,1,2]
    elif ExecutionCase == 10:
            FileName = 'iqr_mu_CPU_Mem_BW'
            ColumnsX =  [0,1,2]
    #-----------------iqr_mu-----------------
    elif ExecutionCase == 11:
            FileName = 'iqr_rs_CPU_MIPS_BW'
            ColumnsX = [0,1,2]
    elif ExecutionCase == 12:
            FileName = 'iqr_rs_CPU_Energy_MIPS_BW_Mem'
            ColumnsX = [0,1,2,3,4]
    elif ExecutionCase == 13:
            FileName = 'iqr_rs_CPU_Storage_BW_Energy'
            ColumnsX = [0,1,2,3]
    elif ExecutionCase == 14:
            FileName = 'iqr_rs_CPU_Mem_BW'
            ColumnsX = [0,1,2]
    #-----------------iqr_rs-----------------
    elif ExecutionCase == 15:
            FileName = 'lr_mc_CPU_Storage_Mem_BW_MIPS_Energy'
            ColumnsX = [0,1,2,3,4,5]
    elif ExecutionCase == 16:
            FileName = 'lr_mc_CPU_BW_Storage_MIPS_Mem'
            ColumnsX =  [0,1,2,3,4]
    elif ExecutionCase == 17:
            FileName = 'lr_mc_CPU_Energy_Storage_MIPS'
            ColumnsX =  [0,1,2,3]
    elif ExecutionCase == 18:
            FileName = 'lr_mc_CPU_BW_MIPS_Mem'
            ColumnsX =  [0,1,2,3]
    elif ExecutionCase == 19:
            FileName = 'lr_mc_CPU_Mem_BW'
            ColumnsX =  [0,1,2]
    #-----------------lr_mc-----------------
    elif ExecutionCase == 20:
            FileName = 'lr_mmt_CPU_MIPS_Energy'
            ColumnsX =  [0,1,2]
    elif ExecutionCase == 21:
            FileName = 'lr_mmt_CPU_BW_Energy'
            ColumnsX =  [0,1,2]
    elif ExecutionCase == 22:
            FileName = 'lr_mmt_CPU_Energy_Storage_Mem'
            ColumnsX =  [0,1,2,3]
    elif ExecutionCase == 23:
            FileName = 'lr_mmt_CPU_BW_MIPS_Mem'
            ColumnsX =  [0,1,2,3]
    elif ExecutionCase == 24:
            FileName = 'lr_mmt_CPU_Mem_BW'
            ColumnsX =  [0,1,2]
    #-----------------lr_mmt-----------------
    elif ExecutionCase == 25:
            FileName = 'lr_mu_CPU_MIPS_Mem_Storage_Energy_BW'
            ColumnsX =  [0,1,2,3,4,5]
    elif ExecutionCase == 26:
            FileName = 'lr_mu_CPU_BW_MIPS'
            ColumnsX =  [0,1,2]
    elif ExecutionCase == 27:
            FileName = 'lr_mu_MIPS_Energy_CPU_Mem_BW'
            ColumnsX =  [0,1,2,3,4]
    elif ExecutionCase == 28:
            FileName = 'lr_mu_CPU_Mem_BW_Storage_Energy_MIPS'
            ColumnsX =  [0,1,2,3,4,5]
    elif ExecutionCase == 29:
            FileName = 'lr_mu_CPU_Mem_BW'
            ColumnsX =  [0,1,2]
    #-----------------lr_mu-----------------
    elif ExecutionCase == 30:
            FileName = 'lr_rs_CPU_Storage_BW_Mem_MIPS_Energy'
            ColumnsX =  [0,1,2,3,4,5]
    elif ExecutionCase == 31:
            FileName = 'lr_rs_CPU_BW_Energy'
            ColumnsX =  [0,1,2]
    elif ExecutionCase == 32:
            FileName = 'lr_rs_Mem_Energy_CPU_MIPS'
            ColumnsX =  [0,1,2,3]
    elif ExecutionCase == 33:
            FileName = 'lr_rs_CPU_Mem_BW_Storage_Energy_MIPS'
            ColumnsX =  [0,1,2,3,4,5]
    elif ExecutionCase == 34:
            FileName = 'lr_rs_CPU_Mem_BW'
            ColumnsX =  [0,1,2]
    #-----------------lr_rs-----------------
    elif ExecutionCase == 35:
            FileName = 'lrr_mc_CPU_Storage_Mem_BW_MIPS_Energy'
            ColumnsX =  [0,1,2,3,4,5]
    elif ExecutionCase == 36:
            FileName = 'lrr_mc_CPU_BW_Storage_MIPS_Mem'
            ColumnsX =  [0,1,2,3,4]
    elif ExecutionCase == 37:
            FileName = 'lrr_mc_CPU_Energy_Storage_MIPS'
            ColumnsX =  [0,1,2,3]
    elif ExecutionCase == 38:
            FileName = 'lrr_mc_CPU_BW_MIPS_Mem'
            ColumnsX =  [0,1,2,3]
    elif ExecutionCase == 39:
            FileName = 'lrr_mc_CPU_Mem_BW'
            ColumnsX =  [0,1,2]
    #-----------------lrr_mc-----------------
    elif ExecutionCase == 40:
            FileName = 'lrr_mmt_CPU_MIPS_Energy'
            ColumnsX =  [0,1,2]
    elif ExecutionCase == 41:
            FileName = 'lrr_mmt_CPU_BW_Energy'
            ColumnsX =  [0,1,2]
    elif ExecutionCase == 42:
            FileName = 'lrr_mmt_CPU_Energy_Storage_Mem'
            ColumnsX =  [0,1,2,3]
    elif ExecutionCase == 43:
            FileName = 'lrr_mmt_CPU_BW_MIPS_Mem_Storage'
            ColumnsX =  [0,1,2,3,4]
    elif ExecutionCase == 44:
            FileName = 'lrr_mmt_CPU_Mem_BW'
            ColumnsX =  [0,1,2]
    #-----------------lrr_mmt-----------------
    elif ExecutionCase == 45:
            FileName = 'lrr_mu_CPU_BW_MIPS'
            ColumnsX =  [0,1,2]
    elif ExecutionCase == 46:
            FileName = 'lrr_mu_MIPS_Energy_CPU_Mem_BW'
            ColumnsX =  [0,1,2,3,4]
    elif ExecutionCase == 47:
            FileName = 'lrr_mu_CPU_BW_MIPS_Mem_Storage'
            ColumnsX =  [0,1,2,3,4]
    elif ExecutionCase == 48:
            FileName = 'lrr_mu_CPU_Mem_BW'
            ColumnsX =  [0,1,2]
    #-----------------lrr_mu-----------------
    elif ExecutionCase == 49:
            FileName = 'lrr_rs_CPU_Mem_BW_MIPS_Energy_Storage'
            ColumnsX =  [0,1,2,3,4,5]
    elif ExecutionCase == 50:
            FileName = 'lrr_rs_CPU_BW_Storage'
            ColumnsX =  [0,1,2]
    elif ExecutionCase == 51:
            FileName = 'lrr_rs_CPU_Energy_Storage'
            ColumnsX =  [0,1,2]
    elif ExecutionCase == 52:
            FileName = 'lrr_rs_CPU_BW_MIPS_Mem_Storage'
            ColumnsX =  [0,1,2,3,4]
    elif ExecutionCase == 53:
            FileName = 'lrr_rs_CPU_Mem_BW'
            ColumnsX =  [0,1,2]
    #-----------------lrr_rs-----------------
    elif ExecutionCase == 54:
            FileName = 'mad_mc_CPU_Energy_MIPS'
            ColumnsX =  [0,1,2]
    elif ExecutionCase == 55:
            FileName = 'mad_mc_CPU_Mem_BW'
            ColumnsX =  [0,1,2]
    #-----------------mad_mc-----------------
    elif ExecutionCase == 56:
            FileName = 'mad_mmt_CPU_Energy_Mem_Storage'
            ColumnsX =  [0,1,2,3]
    elif ExecutionCase == 57:
            FileName = 'mad_mmt_CPU_Mem_BW'
            ColumnsX =  [0,1,2]
    #-----------------mad_mmt-----------------
    elif ExecutionCase == 58:
            FileName = 'mad_mu_CPU_Energy_Mem_BW'
            ColumnsX =  [0,1,2,3]
    elif ExecutionCase == 59:
            FileName = 'mad_mu_CPU_Mem_BW'
            ColumnsX =  [0,1,2]
    #-----------------mad_rs-----------------
    elif ExecutionCase == 60:
            FileName = 'mad_rs_MIPS_Energy_CPU_Mem_Storage'
            ColumnsX =  [0,1,2,3,4]
    elif ExecutionCase == 61:
            FileName = 'mad_rs_CPU_Mem_BW'
            ColumnsX =  [0,1,2]
    #-----------------ICEIS-----------------
    if ExecutionCase == 62:
            BasePath = 'Dataset/ICEIS'
            FileName = 'iqr_rs_CPU_Mem_BW_Storage'
            ColumnsX =  [0,1,2,3]
    if ExecutionCase == 63:
            BasePath = 'Dataset/ICEIS'
            FileName = 'iqr_rs_CPU_Energy_Storage_BW'
            ColumnsX =  [0,1,2,3]
    if ExecutionCase == 64:
            BasePath = 'Dataset/ICEIS'
            FileName = 'cloudsim_iqr_rs_cpu_mem_bw_storage'
            ColumnsX =  [0,1,2,3]
    if ExecutionCase == 65:
            BasePath = 'Dataset/ICEIS'
            FileName = 'cloudsim_iqr_rs_cpu_energy_storage_bw'
            ColumnsX =  [0,1,2,3]
    ColumnsY = [len(ColumnsX)]
    FeaturesFromDataset = len(ColumnsX)

    mf, conj = getMFsAmount(FeaturesFromDataset)

    CSVFile = f'{BasePath}/{FileName}.csv'
    return FileName, CSVFile, ColumnsX, ColumnsY, mf, conj


def getExecutionCaseEnergy(ExecutionCase):
    FileName = ''
    BasePath = 'Dataset/ComTratamento/'
    if ExecutionCase == 0:
            BasePath = 'Dataset/'
            FileName = 'IrisDataset'
            ColumnsX =  [0,1,2,3]
            ColumnsY = [4]
    elif ExecutionCase == 2:
            FileName = 'iqr_mc_CPU_Energy_MIPS'
            ColumnsX =  [0,2]
            ColumnsY = [1]
    elif ExecutionCase == 6:
            FileName = 'iqr_mmt_CPU_Energy_Mem_Storage'
            ColumnsX = [0,2,3]
            ColumnsY = [1]
    #-----------------iqr_mmt-----------------
    elif ExecutionCase == 9:
            FileName = 'iqr_mu_MIPS_Energy_CPU'
            ColumnsX =  [0,2]
            ColumnsY = [1]
    #-----------------iqr_mu-----------------
    elif ExecutionCase == 12:
            FileName = 'iqr_rs_CPU_Energy_MIPS_BW_Mem'
            ColumnsX = [0,2,3,4]
            ColumnsY = [1]
    elif ExecutionCase == 13:
            FileName = 'iqr_rs_CPU_Storage_BW_Energy'
            ColumnsX = [0,1,2]
            ColumnsY = [3]
    #-----------------iqr_rs-----------------
    elif ExecutionCase == 15:
            FileName = 'lr_mc_CPU_Storage_Mem_BW_MIPS_Energy'
            ColumnsX = [0,1,2,3,4]
            ColumnsY = [5]
    elif ExecutionCase == 17:
            FileName = 'lr_mc_CPU_Energy_Storage_MIPS'
            ColumnsX =  [0,2,3]
            ColumnsY = [1]
    #-----------------lr_mc-----------------
    elif ExecutionCase == 20:
            FileName = 'lr_mmt_CPU_MIPS_Energy'
            ColumnsX =  [0,1]
            ColumnsY = [2]
    elif ExecutionCase == 21:
            FileName = 'lr_mmt_CPU_BW_Energy'
            ColumnsX =  [0,1]
            ColumnsY = [2]
    elif ExecutionCase == 22:
            FileName = 'lr_mmt_CPU_Energy_Storage_Mem'
            ColumnsX =  [0,2,3]
            ColumnsY = [1]
    #-----------------lr_mmt-----------------
    elif ExecutionCase == 25:
            FileName = 'lr_mu_CPU_MIPS_Mem_Storage_Energy_BW'
            ColumnsX =  [0,1,2,3,5]
            ColumnsY = [4]
    elif ExecutionCase == 27:
            FileName = 'lr_mu_MIPS_Energy_CPU_Mem_BW'
            ColumnsX =  [0,2,3,4]
            ColumnsY = [1]
    elif ExecutionCase == 28:
            FileName = 'lr_mu_CPU_Mem_BW_Storage_Energy_MIPS'
            ColumnsX =  [0,1,2,3,5]
            ColumnsY = [4]
    #-----------------lr_mu-----------------
    elif ExecutionCase == 30:
            FileName = 'lr_rs_CPU_Storage_BW_Mem_MIPS_Energy'
            ColumnsX =  [0,1,2,3,4]
            ColumnsY = [5]
    elif ExecutionCase == 31:
            FileName = 'lr_rs_CPU_BW_Energy'
            ColumnsX =  [0,1]
            ColumnsY = [2]
    elif ExecutionCase == 32:
            FileName = 'lr_rs_Mem_Energy_CPU_MIPS'
            ColumnsX =  [0,2,3]
            ColumnsY = [1]
    elif ExecutionCase == 33:
            FileName = 'lr_rs_CPU_Mem_BW_Storage_Energy_MIPS'
            ColumnsX =  [0,1,2,3,5]
            ColumnsY = [4]
    #-----------------lr_rs-----------------
    elif ExecutionCase == 35:
            FileName = 'lrr_mc_CPU_Storage_Mem_BW_MIPS_Energy'
            ColumnsX =  [0,1,2,3,4]
            ColumnsY = [5]
    elif ExecutionCase == 37:
            FileName = 'lrr_mc_CPU_Energy_Storage_MIPS'
            ColumnsX =  [0,2,3]
            ColumnsY = [1]
    #-----------------lrr_mc-----------------
    elif ExecutionCase == 40:
            FileName = 'lrr_mmt_CPU_MIPS_Energy'
            ColumnsX =  [0,1]
            ColumnsY = [2]
    elif ExecutionCase == 41:
            FileName = 'lrr_mmt_CPU_BW_Energy'
            ColumnsX =  [0,1]
            ColumnsY = [2]
    elif ExecutionCase == 42:
            FileName = 'lrr_mmt_CPU_Energy_Storage_Mem'
            ColumnsX =  [0,2,3]
            ColumnsY = [1]
    #-----------------lrr_mmt-----------------
    elif ExecutionCase == 46:
            FileName = 'lrr_mu_MIPS_Energy_CPU_Mem_BW'
            ColumnsX =  [0,2,3,4]
            ColumnsY = [1]
    #-----------------lrr_mu-----------------
    elif ExecutionCase == 49:
            FileName = 'lrr_rs_CPU_Mem_BW_MIPS_Energy_Storage'
            ColumnsX =  [0,1,2,3,5]
            ColumnsY = [4]
    elif ExecutionCase == 51:
            FileName = 'lrr_rs_CPU_Energy_Storage'
            ColumnsX =  [0,2]
            ColumnsY = [1]
    #-----------------lrr_rs-----------------
    elif ExecutionCase == 54:
            FileName = 'mad_mc_CPU_Energy_MIPS'
            ColumnsX =  [0,2]
            ColumnsY = [1]
    #-----------------mad_mc-----------------
    elif ExecutionCase == 56:
            FileName = 'mad_mmt_CPU_Energy_Mem_Storage'
            ColumnsX =  [0,2,3]
            ColumnsY = [1]
    #-----------------mad_mmt-----------------
    elif ExecutionCase == 58:
            FileName = 'mad_mu_CPU_Energy_Mem_BW'
            ColumnsX =  [0,2,3]
            ColumnsY = [1]
    #-----------------mad_rs-----------------
    elif ExecutionCase == 60:
            FileName = 'mad_rs_MIPS_Energy_CPU_Mem_Storage'
            ColumnsX =  [0,2,3,4]
            ColumnsY = [1]

    FeaturesFromDataset = len(ColumnsX)

    mf, conj = getMFsAmount(FeaturesFromDataset)

    CSVFile = f'{BasePath}/{FileName}.csv'
    return FileName, CSVFile, ColumnsX, ColumnsY, mf, conj

def getMFsAmount(FeaturesFromDataset):
    mf = []
    conj = []
    if FeaturesFromDataset == 2:
        mf = [
            [['gaussmf',{'mean':0.0,'sigma':0.15}],['gaussmf',{'mean':0.5,'sigma':0.15}],['gaussmf',{'mean':1.0,'sigma':0.15}]],
            [['gaussmf',{'mean':0.0,'sigma':0.15}],['gaussmf',{'mean':0.5,'sigma':0.15}],['gaussmf',{'mean':1.0,'sigma':0.15}]]
        ]
    if FeaturesFromDataset == 3:
        mf = [
            [['gaussmf',{'mean':0.0,'sigma':0.15}],['gaussmf',{'mean':0.5,'sigma':0.15}],['gaussmf',{'mean':1.0,'sigma':0.15}]],
            [['gaussmf',{'mean':0.0,'sigma':0.15}],['gaussmf',{'mean':0.5,'sigma':0.15}],['gaussmf',{'mean':1.0,'sigma':0.15}]],
            [['gaussmf',{'mean':0.0,'sigma':0.15}],['gaussmf',{'mean':0.5,'sigma':0.15}],['gaussmf',{'mean':1.0,'sigma':0.15}]]
        ]
    elif FeaturesFromDataset == 4:
        mf = [
            [['gaussmf',{'mean':0.0,'sigma':0.15}],['gaussmf',{'mean':0.5,'sigma':0.15}],['gaussmf',{'mean':1.0,'sigma':0.15}]],
            [['gaussmf',{'mean':0.0,'sigma':0.15}],['gaussmf',{'mean':0.5,'sigma':0.15}],['gaussmf',{'mean':1.0,'sigma':0.15}]],
            [['gaussmf',{'mean':0.0,'sigma':0.15}],['gaussmf',{'mean':0.5,'sigma':0.15}],['gaussmf',{'mean':1.0,'sigma':0.15}]],
            [['gaussmf',{'mean':0.0,'sigma':0.15}],['gaussmf',{'mean':0.5,'sigma':0.15}],['gaussmf',{'mean':1.0,'sigma':0.15}]]
        ]
        #mf = [
        #  [['gaussmf',{'mean':0.,'sigma':1.}],
        #   ['gaussmf',{'mean':-1.,'sigma':2.}],
        #   ['gaussmf',{'mean':-4.,'sigma':10.}]],
        #  [['gaussmf',{'mean':1.,'sigma':2.}],
        #   ['gaussmf',{'mean':2.,'sigma':3.}], 
        #   ['gaussmf',{'mean':-2.,'sigma':10.}]],
        #  [['gaussmf',{'mean':1.,'sigma':2.}],
        #   ['gaussmf',{'mean':2.,'sigma':3.}], 
        #   ['gaussmf',{'mean':-2.,'sigma':10.}]],
        #  [['gaussmf',{'mean':1.,'sigma':2.}],
        #   ['gaussmf',{'mean':2.,'sigma':3.}], 
        #   ['gaussmf',{'mean':-2.,'sigma':10.}]
        #   ]]
    elif FeaturesFromDataset == 5:
        mf = [
            [['gaussmf',{'mean':0.0,'sigma':0.15}],['gaussmf',{'mean':0.5,'sigma':0.15}],['gaussmf',{'mean':1.0,'sigma':0.15}]],
            [['gaussmf',{'mean':0.0,'sigma':0.15}],['gaussmf',{'mean':0.5,'sigma':0.15}],['gaussmf',{'mean':1.0,'sigma':0.15}]],
            [['gaussmf',{'mean':0.0,'sigma':0.15}],['gaussmf',{'mean':0.5,'sigma':0.15}],['gaussmf',{'mean':1.0,'sigma':0.15}]],
            [['gaussmf',{'mean':0.0,'sigma':0.15}],['gaussmf',{'mean':0.5,'sigma':0.15}],['gaussmf',{'mean':1.0,'sigma':0.15}]],
            [['gaussmf',{'mean':0.0,'sigma':0.15}],['gaussmf',{'mean':0.5,'sigma':0.15}],['gaussmf',{'mean':1.0,'sigma':0.15}]]
        ]
    elif FeaturesFromDataset == 6:
        mf = [
            [['gaussmf',{'mean':0.0,'sigma':0.15}],['gaussmf',{'mean':0.5,'sigma':0.15}],['gaussmf',{'mean':1.0,'sigma':0.15}]],
            [['gaussmf',{'mean':0.0,'sigma':0.15}],['gaussmf',{'mean':0.5,'sigma':0.15}],['gaussmf',{'mean':1.0,'sigma':0.15}]],
            [['gaussmf',{'mean':0.0,'sigma':0.15}],['gaussmf',{'mean':0.5,'sigma':0.15}],['gaussmf',{'mean':1.0,'sigma':0.15}]],
            [['gaussmf',{'mean':0.0,'sigma':0.15}],['gaussmf',{'mean':0.5,'sigma':0.15}],['gaussmf',{'mean':1.0,'sigma':0.15}]],
            [['gaussmf',{'mean':0.0,'sigma':0.15}],['gaussmf',{'mean':0.5,'sigma':0.15}],['gaussmf',{'mean':1.0,'sigma':0.15}]],
            [['gaussmf',{'mean':0.0,'sigma':0.15}],['gaussmf',{'mean':0.5,'sigma':0.15}],['gaussmf',{'mean':1.0,'sigma':0.15}]]
        ]
    
    conj = ['baixo', 'medio', 'alto']
    return mf, conj