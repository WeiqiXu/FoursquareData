Code:
dataPreprocessing.py is for data preprocessing
prediction.py is for POI prediction 

Dataset:
The dataset is stored at:
https://drive.google.com/drive/folders/1dGpspvtLdqfWD0_UBoD4LxidZTEYEJ9k?usp=sharing

"CA dataset/check_CA_venues.txt" contains check-in records, each entry is in the form of:
{userID, Time(GMT), VenueId, VenueName, VenueLocation, VenueCategory}
where:
  "Time(GMT)" is check-in time in GMT format
  "VenueId" is the check-in venue, which corresponds to Foursquare venue ID

"CA dataset/fs_friendship_CA.txt" contains indirect social connections among these users. All the users involved in this dataset are from California (according to the hometown information from their profiles on Foursquare).

The "/res" folder contains the embedding results of the barpartite graphs in the model.
Please feel free to discuss with me if you have any questions about the dataset.
