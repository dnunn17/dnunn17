// Fill out your copyright notice in the Description page of Project Settings.


#include "FolderColors.h"
#include "Runtime/Core/Public/Misc/ConfigCacheIni.h"

void UFolderColors::SetFolderColor(FString FolderPath, FLinearColor Color) {
	GConfig->SetString(TEXT("PathColor"), *FolderPath, *Color.ToString(), GEditorPerProjectIni);
}