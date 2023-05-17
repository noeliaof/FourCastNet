#!/bin/bash

#SBATCH --mem=128G
#SBATCH --nodes=1
#SBATCH --time=12:00:00
#SBATCH --partition=gpu
#SBATCH --qos=job_gpu_preempt
#SBATCH --gres=gpu:rtx3090:4

module load Workspace
module load Anaconda3
module load CUDA/11.8.0
#module load cuDNN
source activate
conda activate /storage/homefs/no21h426/.conda/envs/cuda_env_clone
#srun python inference/inference.py \
#       --config=afno_backbone \
#       --run_num=0 \
#       --weights '/storage/homefs/no21h426/FourCastNet/FCN_weights_v0/backbone.ckpt' \
#       --override_dir '/storage/homefs/no21h426/FourCastNet/predictions/output/ ' 

srun python inference/inference.py --config=afno_backbone --run_num=0 --vis   \
        --weights '/storage/homefs/no21h426/FourCastNet/FCN_weights_v0/backbone.ckpt' \
        --override_dir '/storage/homefs/no21h426/FourCastNet/output'  
