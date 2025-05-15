const axios = require('axios');

/**
 * 封装 fetch_music 功能
 * @param {string} msg - 歌曲名称，默认为 '红豆'
 * @returns {Promise<{share_url: string, track_id: string, song_name: string}>}
 */
async function fetchMusic(msg = '红豆') {
    const url = 'https://api.ilingku.com/int/v1/dg_qishui';
    const requestData = {
        msg,
        format: 'json'
    };

    try {
        const response = await axios.post(url, requestData);
        const result = response.data;
        let trackId = null;
        let songName = null;

        if (typeof result === 'object' && result.data) {
            const data = result.data;
            if (Array.isArray(data)) {
                for (const item of data) {
                    if (typeof item === 'object') {
                        trackId = item.track_id;
                        songName = item.title;
                        if (trackId) {
                            break;
                        }
                    }
                }
            }
        }

        let shareUrl;
        if (trackId) {
            shareUrl = `https://music.douyin.com/qishui/share/track?track_id=${trackId}`;
            console.log(shareUrl);
        } else {
            console.log('未找到有效的 track_id');
        }

        return { share_url: shareUrl, track_id: trackId, song_name: songName };
    } catch (err) {
        console.error(`下载文件时发生其他错误: ${err}`);
        throw err;
    }
}

/**
 * Serverless 处理函数
 * @param {Object} event - 事件对象
 * @param {Object} context - 上下文对象
 * @returns {Promise<{statusCode: number, body: string}>}
 */
module.exports.handler = async (event, context) => {
    try {
        const { msg } = event;
        const { share_url, track_id, song_name } = await fetchMusic(msg);
        return {
            statusCode: 200,
            body: JSON.stringify({ share_url, track_id, song_name })
        };
    } catch (error) {
        return {
            statusCode: 500,
            body: JSON.stringify({ error: error.message })
        };
    }
}