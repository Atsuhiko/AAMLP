# config.py 

# config.py 
import transformers
from transformers import BertTokenizer, BertModel
 
# this is the maximum number of tokens in the sentence 
MAX_LEN = 512 
 
# batch sizes is small because model is huge! 
TRAIN_BATCH_SIZE = 8 
VALID_BATCH_SIZE = 4 
 
# let's train for a maximum of 10 epochs 
EPOCHS = 10 
 
# define path to BERT model files 
BERT_PATH = "bert-base-uncased/" 
 
# this is where you want to save the model 
MODEL_PATH = "model.bin" 
 
# training file 
TRAINING_FILE = "imdb_folds.csv" 
 
# define the tokenizer 
# we use tokenizer and model  
# from huggingface's transformers 
TOKENIZER = BertTokenizer.from_pretrained(BERT_PATH, do_lower_case=True)
#model = BertModel.from_pretrained("bert-base-uncased")