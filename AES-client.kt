import java.util.Base64
import javax.crypto.Cipher
import javax.crypto.spec.GCMParameterSpec
import javax.crypto.spec.SecretKeySpec

fun main() {
    val encryptedText = "Base64 Encoded String from Server"
    val key = "negarhonarvarsedighianisme------".toByteArray() 

    try {
        val decryptedText = decryptText(encryptedText, key)
        println("Decrypted: $decryptedText")
    } catch (e: Exception) {
        println("Error during decryption: ${e.message}")
    }
}

fun decryptText(encryptedText: String, key: ByteArray): String {
    val decodedBytes = Base64.getDecoder().decode(encryptedText)
    val secretKey = SecretKeySpec(key, "AES")

    val nonceSize = 12 // AES-GCM standard nonce size
    val nonce = decodedBytes.copyOfRange(0, nonceSize)
    val cipherText = decodedBytes.copyOfRange(nonceSize, decodedBytes.size)

    val cipher = Cipher.getInstance("AES/GCM/NoPadding")
    val spec = GCMParameterSpec(128, nonce) // 128-bit auth tag length
    cipher.init(Cipher.DECRYPT_MODE, secretKey, spec)

    val plaintext = cipher.doFinal(cipherText)
    return String(plaintext)
}
