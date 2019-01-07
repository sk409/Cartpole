<h1>自作の機械学習ライブラリで強化学習を行いました。</h1>
<br>
<h2>環境: Open AI Gym (CartPole)</h2>
<br>

<p>DQN, ExperienceReplayなどの技術を用いて約40分間学習させました。</p>
<p>cartpole_main.pyを実行することで実際に学習を行い、学習途中のログを確認することができます。</p>
<p>cartpole_test.pyと同じ階層にmodels/best_model/cartpole_model.pklとフォルダ・ファイルを作り実行することで、モデルを試すことができます。</p>
<p>容量の関係でgithubにはmodelファイルは置いていませんが、以下のリンクからダウンロードしていただくことが可能です。</p>
<br>

<p>以下に今回の学習によって得られた各ファイルへのリンクを示します。</p>
<br>

<p><a href="https://drive.google.com/drive/folders/1KpIJzAR9y2GweXMRbbPOZx7DXVzWqMHd?usp=sharing">学習時に出力されたログ</a></p>
<p>学習が進むごとに長い時間棒を立てた状態を維持できていることがわかります。</p>
<br>

<p><a href="https://drive.google.com/drive/folders/1ZvUbr0Roo7vgKc7CR_LcsXlZRUGGhUOz?usp=sharing">学習済みのモデル</a></p>
<p>自作ライブラリの学習済みモデルです。</p>
<p>cartpole_test.pyと同じ階層にmodels/best_model/cartpole_model.pklとフォルダ・ファイルを作ることでモデルを試すことができます。</p>
<p>以下にモデルを試す方法を視覚的に示します。</p>
<p>cartpole_test.pyと同じ階層にmodelsフォルダを置きます。</p>
<img src="images/image_1.png" width="900" height=700>
<p>modelsフォルダの下に、best_modelフォルダを置きます。</p>
<img src="images/image_2.png" width="900" height=700>
<p>best_modelフォルダの下に、cartpole_model.pklを置きます。</p>
<p>今回学習させたモデルは<a href="https://drive.google.com/file/d/1-XzOqSUWn3CORL8oC0w-9LVNN_k7JPGS/view?usp=sharing">こちら</a>からダウンロードしていただくことが可能です。</p>
<img src="images/image_3.png" width="900" height=700>
<p>最後に、cartpole_test.pyを実行します。</p>
<img src="images/image_4.png" width="900" height=700>
<br>

<p><a href="https://drive.google.com/drive/folders/1Uot_jluqqfir-RdftLyyFrW_78hdRNxi?usp=sharing">学習過程の動画</a></p>
<p>100エピソードごとに保存した、学習過程の動画です。</p>
<p>棒を倒してしまった時点で、動画は終了します。</p>
<p>エピソードが進むごとに長い時間棒を立てた状態を維持できているのが視覚的に確認できます。</p>