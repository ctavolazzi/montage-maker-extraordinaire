# How to work in this repo

CT (Christopher) owns this. He taps play on the notebook in his Drive; it pulls videos from his
iCloud (via icloudpd) plus any in My Drive/Montage Maker, and saves a montage to its Montages
folder. His phone has no free storage, so nothing may go through the phone.

The live copy is in his Drive (file id `1CDqoH_RIn4GRFtCaNTsoEqYmPK8U6TwE`). When
`montage.ipynb` changes here, update that file too.

- **Keep it simple.** One notebook, `montage.ipynb`, run on Google Colab. No settings. Add a
  feature only when CT asks.
- **Free.** No paid APIs. Any AI runs inside the Colab notebook.
- **Works from his phone, computer off.** Nothing may depend on his computer.
- **Never change the uploaded videos.** Write only to the `Montages` folder.
- **No em dashes.**
- Commits go to `main`, small, plain messages. Don't open or watch pull requests unless CT asks.
