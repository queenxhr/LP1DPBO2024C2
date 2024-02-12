//Class delaration. For Java, the first letter MUST BE capitalized.
public class DPR
{
    //Private attributws.
    private String id; // Atribut unruk menampung id anggota DPR
    private String nama; // Atribut unruk menampung nama anggota DPR
    private String bidang; // Atribut unruk menampung bidang anggota DPR
    private String partai; // Atribut unruk menampung partai anggota DPR

    /*Constructors */

    //Constructors. Take note that it doesn't have any return type
    public DPR()
    {
        this.id = "";
        this.nama = "";
        this.bidang = "";
        this.partai = "";
    }

    //Another constructore with parameter.
    public DPR(String id, String nama, String bidang, String partai)
    {
        this.id = id;
        this.nama = nama;
        this.bidang = bidang;
        this.partai = partai;
    }

    /* Getter and Setter */
    
    //Get id.
    public String getId(){
        return this.id;
    }

    //Set id.
    public void setId(String id)
    {
        this.id = id;
    }

    //Get nama.
    public String getnama(){
        return this.nama;
    }

    //Set nama.
    public void setnama(String nama)
    {
        this.nama = nama;
    }

    //Get bidang.
    public String getbidang(){
        return this.bidang;
    }

    //Set bidang.
    public void setbidang(String bidang)
    {
        this.bidang = bidang;
    }

    //Get partai.
    public String getpartai(){
        return this.partai;
    }

    //Set partai.
    public void setpartai(String partai)
    {
        this.partai = partai;
    }

    // Method to display member information
    public void displayInfo() {
        System.out.println("ID: " + id);
        System.out.println("Nama: " + nama);
        System.out.println("Bidang: " + bidang);
        System.out.println("Partai: " + partai);
    }

    
}