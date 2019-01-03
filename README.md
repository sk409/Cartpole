<h1>自作の機械学習ライブラリで強化学習を行いました。</h1>
<br>
<h2>環境: Open AI Gym (CartPole)</h2>
<br>

<p>DQN, ExperienceReplayなどの技術を用いて1000エピソード学習させました。</p>
<p>cartpole_main.pyにて学習の詳細を確認することができます。</p>
<br>

<p>以下に今回の学習によって得られた各ファイルへのリンクを示します。</p>
<br>

<p><a href="https://drive.google.com/drive/folders/1KpIJzAR9y2GweXMRbbPOZx7DXVzWqMHd?usp=sharing">学習時に出力されたログ</a></p>
<p>学習が進むごとに長い時間棒を立てた状態を維持できていることがわかります。</p>
<br>

<p><a href="https://drive.google.com/drive/folders/1ZvUbr0Roo7vgKc7CR_LcsXlZRUGGhUOz?usp=sharing">学習済みのモデル</a></p>
<p>自作ライブラリの学習済みモデルです。</p>
<p>cartpole_test.pyと同じ階層にmodels/best_model/cartpole_model.pklとフォルダ・ファイルを作ることでモデルを試すことができます。</p>
<p>詳しくはcartpole_test.pyをご覧ください。</p>
<br>

<p><a href="https://drive.google.com/drive/folders/1Uot_jluqqfir-RdftLyyFrW_78hdRNxi?usp=sharing"></a></p>
<p>学習過程の動画です。</p>
<p>エピソードが進むごとに長い時間棒を立てた状態を維持できているのが視覚的に確認できます。</p>