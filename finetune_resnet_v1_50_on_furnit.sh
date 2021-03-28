set -e
# Where the pre-trained ResNetV1-50 checkpoint is saved to.
PRETRAINED_CHECKPOINT_DIR=/home/ailab/Documents/Uday/tensorflow/models/research/slim/data/pretrained_checkpoints
MODEL_NAME=resnet_v1_50
# Where the training (fine-tuned) checkpoint and logs will be saved to.
TRAIN_DIR=/home/ailab/Documents/Uday/tensorflow/models/research/slim/data/furnit/train_resnetv1_orig2/${MODEL_NAME}
# Where test dataset is present 
TEST_DATA_DIR=/home/ailab/Documents/Uday/tensorflow/models/research/slim/data/furnit/test_dir
# Where the dataset is saved to.
DATASET_DIR=/home/ailab/Documents/Uday/tensorflow/models/research/slim/data/furnit
if false
then
# Fine-tune only the new layers for 3000 steps.
python train_image_classifier.py \
  --train_dir=${TRAIN_DIR} \
  --dataset_name=furnit \
  --dataset_split_name=train \
  --dataset_dir=${DATASET_DIR} \
  --model_name=resnet_v1_50 \
  --checkpoint_path=${PRETRAINED_CHECKPOINT_DIR}/resnet_v1_50.ckpt \
  --checkpoint_exclude_scopes=resnet_v1_50/logits \
  --trainable_scopes=resnet_v1_50/logits \
  --max_number_of_steps=210000   
fi
if false
then
python eval_image_classifier.py \
  --checkpoint_path=${TRAIN_DIR} \
  --eval_dir=${TRAIN_DIR} \
  --dataset_name=furnit \
  --dataset_split_name=validation \
  --dataset_dir=${DATASET_DIR} \
  --model_name=resnet_v1_50
fi
if true
then
python eval_image_classifier.py \
  --checkpoint_path=${TRAIN_DIR} \
  --eval_dir=${TEST_DATA_DIR} \
  --dataset_name=furnit \
  --dataset_split_name=validation \
  --dataset_dir=${TEST_DATA_DIR} \
  --model_name=resnet_v1_50
fi


if false
then
# Fine-tune only the new layers for 3000 steps.
python train_image_classifier.py \
  --train_dir=${TRAIN_DIR} \
  --dataset_name=furnit \
  --dataset_split_name=train \
  --dataset_dir=${DATASET_DIR} \
  --model_name=resnet_v1_50 \
  --checkpoint_path=${PRETRAINED_CHECKPOINT_DIR}/resnet_v1_50.ckpt \
  --checkpoint_exclude_scopes=resnet_v1_50/logits \
  --trainable_scopes=resnet_v1_50/logits \
  --max_number_of_steps=60000 \
  --batch_size=32 \
  --learning_rate=0.01 \
  --save_interval_secs=60 \
  --save_summaries_secs=60 \
  --log_every_n_steps=100 \
  --optimizer=rmsprop \
  --weight_decay=0.00004

# Run evaluation.
python eval_image_classifier.py \
  --checkpoint_path=${TRAIN_DIR} \
  --eval_dir=${TRAIN_DIR} \
  --dataset_name=flowers \
  --dataset_split_name=validation \
  --dataset_dir=${DATASET_DIR} \
  --model_name=resnet_v1_50

# Fine-tune all the new layers for 1000 steps.
python train_image_classifier.py \
  --train_dir=${TRAIN_DIR}/all \
  --dataset_name=flowers \
  --dataset_split_name=train \
  --dataset_dir=${DATASET_DIR} \
  --checkpoint_path=${TRAIN_DIR} \
  --model_name=resnet_v1_50 \
  --max_number_of_steps=1000 \
  --batch_size=32 \
  --learning_rate=0.001 \
  --save_interval_secs=60 \
  --save_summaries_secs=60 \
  --log_every_n_steps=100 \
  --optimizer=rmsprop \
  --weight_decay=0.00004

# Run evaluation.
python eval_image_classifier.py \
  --checkpoint_path=${TRAIN_DIR}/all \
  --eval_dir=${TRAIN_DIR}/all \
  --dataset_name=flowers \
  --dataset_split_name=validation \
  --dataset_dir=${DATASET_DIR} \
  --model_name=resnet_v1_50
fi
