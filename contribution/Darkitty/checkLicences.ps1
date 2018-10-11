#########################################################################################
# Script pour vérifier l'état des licences Windows                                      #
# Auteur : Nicolas LE GALL                                                              #
# Date : 17/09/2015                                                                     #
#########################################################################################


$mycred = Get-Credential
# DC
if(($dc = (Get-ADDomainController).Name) -eq "") { Write-Host "Aucun serveur DC trouvé"; exit -1 }

$PCs = Invoke-Command -ComputerName $dc -ScriptBlock { (Get-ADComputer -Filter *).Name } -credential $mycred
$serveurs = Invoke-Command -ComputerName $dc -ScriptBlock { (Get-ADComputer -Filter * -SearchBase "OU=Serveurs,DC=domain,DC=tld").Name } -credential $mycred

Remove-Item "licencestatus.csv"
Add-Content "licencestatus.csv" "Nom;Type;Status licence"

foreach($PC in $PCs)
{
    Write-Host $PC
    $licenceStatus = (Get-WmiObject -Query "Select * from SoftwareLicensingProduct Where PartialProductKey IS NOT NULL AND ApplicationID = '55c92734-d682-4d71-983e-d6ec3f16059f'" -ComputerName $PC -Credential $mycred).LicenseStatus

    Switch ($licenceStatus)
    {
        0 { $statusName = "Unlicensed" }
        1 { $statusName = "Licensed" }
        2 { $statusName = "Out-of-Box Grace Period" }
        3 { $statusName = "Out-of-Tolerance Grace Period" }
        4 { $statusName = "Non-Genuine Grace Period" }
        5 { $statusName = "Notification" }
        6 { $statusName = "ExtendedGrace" }
    }
    
    $type = "Ordinateur"
    if ($serveurs.Contains($PC)) { $type = "Serveur" }

    Add-Content "licencestatus.csv" "$PC;$type;$statusName"
}
