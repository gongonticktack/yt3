/**
 * 概要:
 *   ページの読み込みが終わったあと、変換フォームの送信中表示を設定します。
 * 引数:
 *   ありません。
 * 戻り値:
 *   ありません。
 */
document.addEventListener('DOMContentLoaded', () => {
  // 画面にある最初のフォームを探します。
  const form = document.querySelector('form');
  if (!form) {
    return;
  }

  /**
   * 概要:
   *   変換ボタンが押されたら、押されたボタンの文字を変えて二重クリックを防ぎます。
   * 引数:
   *   event: フォーム送信時にブラウザから渡されるイベント情報です。
   * 戻り値:
   *   ありません。
   */
  form.addEventListener('submit', (event) => {
    // MP3とMP4のどちらが押されたかをブラウザから受け取ります。
    const submitButton = event.submitter || form.querySelector('button');
    if (submitButton) {
      submitButton.textContent = 'Converting...';

      // 送信する値が消えないよう、送信開始の直後にボタンを無効化します。
      setTimeout(() => {
        submitButton.disabled = true;
      }, 0);
    }
  });
});
